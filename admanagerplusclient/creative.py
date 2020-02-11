import json
import time

from admanagerplusclient.base import Base


class Creative(Base):
    def get_creatives_by_lineitem(self, lineitem_id, seat_id):
        endpoint = f"{self.dsp_host}/traffic/ads/"
        creatives = []
        params = {
            "lineId": lineitem_id,
            "seatId": str(seat_id),
            "limit": 100,
            "page": 0
        }

        while True:
            params["page"] += 1
            expected_total = params["page"] * params["limit"]

            response = json.loads(self.make_request(endpoint, self.headers, 'GET', params=params))

            if response.get('msg_type') == "error":
                validation_messages = response.get('data').get('validationMessages', [])
                # to check error response
                if len(validation_messages) == 0:
                    print("")
                    print("")
                    print("")
                    print("Error hit but no message received")
                    print(response.get('data'))
                    print("")
                    print("")
                    print("")

                for error in validation_messages:
                    if error.get('propertyName') == "RPM":
                        print("")
                        print("")
                        print("")
                        print("Traffic Limit Exceeded Sleeping...")
                        time.sleep(61)
                        print("")
                        print("")
                        print("")

                        response = json.loads(self.make_request(endpoint, self.headers, 'GET', params=params))

            if response.get('msg_type') == "success":
                for creative in response.get('data').get('response'):
                    creatives.append(creative)

            if int(len(creatives)) != int(expected_total):
                break

        response['data'] = creatives

        return json.dumps(response)

    def get_one(self, creative_id, seat_id):
        url = f"{self.dsp_host}/traffic/ads/{str(creative_id)}/"
        params = {
            "seatId": str(seat_id)
        }

        r = self.make_request(url, self.headers, 'GET', params=params)
        return r
