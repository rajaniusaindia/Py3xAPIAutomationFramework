# Check out previous test case Lab187 - conftest.py - create_booking_id
# We divided it into 5 parts -
# Create Helpers - requests wrapper, verification and the payload manager

import allure
import pytest

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_request
from src.helpers.common_verification import verfiy_http_status_code, verify_json_key_for_not_null
from src.helpers.payload_manager import payload_create_booking
from src.utils.utils import Utils

class TestCreateBooking(object):
    @pytest.mark.positive
    @allure.title("Verify that Create Booking Status and Booking ID should not be null ")
    @allure.description(
        "Creating a Booking from the payload and verify that booking id should not be null")

    def test_create_booking_positive(self):
        response = post_request(url=APIConstants().url_create_booking(),
                                auth=None,
                                headers=Utils().common_headers_json(),
                                payload=payload_create_booking(),
                                in_json=False)

        verfiy_http_status_code(response_data=response, expect_data=200)
        verify_json_key_for_not_null(response.json()["bookingid"])


    # 1st it was - pass - future implementation
    # run this test case first before proceeding with any push of code to the github