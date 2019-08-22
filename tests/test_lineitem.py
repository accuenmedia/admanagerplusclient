import config
import json

import unittest

from admanagerplusclient.connection import Connection
from admanagerplusclient.lineitem import LineItem

class LineItemTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.connection = Connection(config.client_id, config.client_secret, config.refresh_token)

    def test_get_all_lines_by_campaign(self):
        l = LineItem(LineItemTestCase.connection)

        lines = json.loads(l.get_lines_by_campaign_id(97893, 92))
        # print(lines)

        self.assertEqual(lines["response_code"], 200)

    def test_get_one_lineitem(self):
        l = LineItem(LineItemTestCase.connection)

        line = json.loads(l.get_one(376875, 92))
        # print(line)

        self.assertEqual(line["response_code"], 200)

    def test_update_one_lineitem(self):
        l = LineItem(LineItemTestCase.connection)

        line = json.loads(l.get_one(323105, 92))
        line_data = line["data"]["response"]

        settings = {
            'status': line_data["status"],
            'pacingModeType': line_data["pacingModeType"],
            'mediaType': line_data["mediaType"],
            'goalType': line_data["goalType"],
            'billingMethodType': line_data["billingMethodType"],
            'budgetType': line_data["budgetType"],
            'dailyBudgetType': line_data["dailyBudgetType"],
            'marginType': line_data["marginType"],
            # 8/22/19: schedule is currently broken in the Verizon API
            # 'schedule': {
                # 'startDateStr': line_data["schedule"]["startDateStr"],
                # 'endDateStr': line_data["schedule"]["endDateStr"],
            #     'id': line_data["schedule"]["id"],
            #     'budget': line_data["schedule"]["budget"]
            # },
            'id': line_data["id"],
            'name': line_data["name"],
            'orderId': line_data["orderId"],
            'bidPrice': line_data["bidPrice"],
            'dailyBudget': line_data["dailyBudget"],
            'billingPrice': line_data["billingPrice"],
            'isNativeEnabled': line_data["isNativeEnabled"],
            'completionThreshold': line_data["completionThreshold"]
        }

        updated_line = json.loads(l.update_one(323105, settings, 92))
        print(updated_line)

        self.assertEqual(updated_line["response_code"], 200)

