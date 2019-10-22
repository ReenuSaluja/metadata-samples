# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Request(Model):
    """Request.

    :param name:
    :type name: str
    :param type_name:
    :type type_name: str
    :param qualified_name:
    :type qualified_name: str
    :param created_by:
    :type created_by: str
    :param process_attributes:
    :type process_attributes: list[~swagger.models.ProcessAttributes]
    :param inputs:
    :type inputs: list[~swagger.models.Inputs]
    :param outputs:
    :type outputs: list[~swagger.models.Outputs]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type_name': {'key': 'type_name', 'type': 'str'},
        'qualified_name': {'key': 'qualified_name', 'type': 'str'},
        'created_by': {'key': 'created_by', 'type': 'str'},
        'process_attributes': {'key': 'process_attributes', 'type': '[ProcessAttributes]'},
        'inputs': {'key': 'inputs', 'type': '[Inputs]'},
        'outputs': {'key': 'outputs', 'type': '[Outputs]'},
    }

    def __init__(self, *, name: str=None, type_name: str=None, qualified_name: str=None, created_by: str=None, process_attributes=None, inputs=None, outputs=None, **kwargs) -> None:
        super(Request, self).__init__(**kwargs)
        self.name = name
        self.type_name = type_name
        self.qualified_name = qualified_name
        self.created_by = created_by
        self.process_attributes = process_attributes
        self.inputs = inputs
        self.outputs = outputs