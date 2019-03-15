import json

class ObjDict(dict):
    """Dict object where keys are field names"""

    def __getattr__(self, name):
        if name in self:
            return self[name]
        else:
            raise AttributeError("No such attribute: " + name)

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        if name in self:
            del self[name]
        else:
            raise AttributeError("No such attribute: " + name)

class Node(object):
    def __init__(self, entity, version):
        self.version = version
        self.entity = entity
        self.inputs = set()
        self.outputs = set()

    @property
    def uuid(self):
        return self.entity.provenance.document_id

    @property
    def fqid(self):
        return "{}.{}".format(self.uuid, self.version)

class Process(Node):
    has_dag_provenance = True

    def __init__(self, entity, version):
        super().__init__(entity, version)
        self.protocols = set()


class Protocol(Node):
    has_dag_provenance = False

    def __init__(self, entity, version):
        super().__init__(entity, version)

class Product(Node):
    """Files, biomaterial, etc """
    has_dag_provenance = True

    def __init__(self, entity, version):
        super().__init__(entity, version)

    def is_supplementary_file(self):
        return self.entity.describedBy.endswith("/supplementary_file")

class Project(Node):
    """Graph for entire project.  The inputs and outputs arrays are initial and terminal nodes.
    Can delay setting entity and version."""

    has_dag_provenance = False
    def __init__(self, entity=None, version=None):
        super().__init__(entity, version)
        self.nodes_by_uuid = {}
        self.supplementary_files_by_fqid = {}

    def add_node(self, node):
        """records the existence of the node in the project, but does no other linking"""
        if node.uuid in self.nodes_by_uuid:
            raise Exception("{} node {} already exists in project, versions not yet supported"
                            .format(node.entity.schema_type, node.uuid))
        self.nodes_by_uuid[node.uuid] = node

    def add_supplementary_file(self, node):
        self.supplementary_files_by_fqid[node.fqid] = node

    def write_to_json(self, fh):
        "write as an array of entities"
        entities = [n.entity for n in self.nodes_by_uuid.values()]
        json.dump(entities, fh, indent=4, sort_keys=True)


def node_factory(entity, version):
    st = entity.schema_type
    if st == "project":
        return Project(entity, version)
    elif st == "process":
        return Process(entity, version)
    elif st == "protocol":
        return Protocol(entity, version)
    else:
        return Product(entity, version)

def fqid_to_uuid(fqid):
    """turn a fqid to a uuid.  If there isn't a version uuid is passed back"""
    return fqid.split('.')[0]
