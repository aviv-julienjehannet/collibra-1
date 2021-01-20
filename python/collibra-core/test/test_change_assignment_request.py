"""
    Collibra Data Governance Center Core API

    <p>The Core REST API allows you to create your own integrations with Collibra Data Governance Center.</p><p><i>Create custom applications to help users get access to the right data.</i></p>  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import collibra_core
from collibra_core.model.articulation_rule_request import ArticulationRuleRequest
from collibra_core.model.characteristic_type_assignment_reference import CharacteristicTypeAssignmentReference
globals()['ArticulationRuleRequest'] = ArticulationRuleRequest
globals()['CharacteristicTypeAssignmentReference'] = CharacteristicTypeAssignmentReference
from collibra_core.model.change_assignment_request import ChangeAssignmentRequest


class TestChangeAssignmentRequest(unittest.TestCase):
    """ChangeAssignmentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testChangeAssignmentRequest(self):
        """Test ChangeAssignmentRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ChangeAssignmentRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()