# CHeck out previous test case Lab187 - conftest.py - create_booking_id
# We divided it into 5 parts -
# Create Helpers - requests wrapper, verification and the payload manager

import allure
import pytest

class TestCreateBooking(object):
    @pytest.mark.positive
    @allure.title("Verify that Create Booking Status and Booking ID should not be null ")
    @allure.description(
        "Creating a Booking from the payload and verify that booking id should not be null")

    def test_create_booking_positive(self):
        pass
    # run this test case first before proceeding with any push of code to the github