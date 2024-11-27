import unittest
from datetime import datetime
from unittest.mock import patch, Mock, PropertyMock
import mock.GPIO as GPIO
from mock.SDL_DS3231 import SDL_DS3231
from mock.adafruit_veml7700 import VEML7700
from src.intelligentoffice import IntelligentOffice, IntelligentOfficeError


class TestIntelligentOffice(unittest.TestCase):

    @patch.object(GPIO, "input")
    def test_person_in_room_pin1(self, mock_pin_1: Mock):
        mock_pin_1.return_value = True
        io = IntelligentOffice()
        self.assertTrue(io.check_quadrant_occupancy(io.INFRARED_PIN1))

    @patch.object(GPIO, "input")
    def test_person_in_room_pin2(self, mock_pin_2: Mock):
        mock_pin_2.return_value = True
        io = IntelligentOffice()
        self.assertTrue(io.check_quadrant_occupancy(io.INFRARED_PIN2))

    @patch.object(GPIO, "input")
    def test_person_in_room_pin3(self, mock_pin_3: Mock):
        mock_pin_3.return_value = True
        io = IntelligentOffice()
        self.assertTrue(io.check_quadrant_occupancy(io.INFRARED_PIN3))

    @patch.object(GPIO, "input")
    def test_person_in_room_pin4(self, mock_pin_4: Mock):
        mock_pin_4.return_value = True
        io = IntelligentOffice()
        self.assertTrue(io.check_quadrant_occupancy(io.INFRARED_PIN4))

    @patch.object(GPIO, "input")
    def test_no_person_in_room(self, mock_pin_11: Mock):
        mock_pin_11.return_value = False
        io = IntelligentOffice()
        self.assertFalse(io.check_quadrant_occupancy(io.INFRARED_PIN1))

    @patch.object(GPIO, "input")
    def test_wrong_pin_error(self, mock_pin_11: Mock):
        mock_pin_11.return_value = True
        io = IntelligentOffice()
        self.assertRaises(IntelligentOfficeError, io.check_quadrant_occupancy,14)

    @patch.object(SDL_DS3231, "read_datetime")
    def test_blinds_fully_open_weekday(self, mock_datetime: Mock):
        mock_datetime.return_value = datetime(2024, 11, 16, 16, 10)
        io = IntelligentOffice()
        io.manage_blinds_based_on_time()
        self.assertTrue(io.blinds_open)

    @patch.object(SDL_DS3231, "read_datetime")
    def test_blinds_fully_close_weekend(self, mock_datetime: Mock):
        mock_datetime.return_value = datetime(2024, 11, 25, 16, 10)
        io = IntelligentOffice()
        io.manage_blinds_based_on_time()
        self.assertFalse(io.blinds_open)

    @patch.object(SDL_DS3231, "read_datetime")
    def test_blinds_fully_close_weekday_non_office_hours(self, mock_datetime: Mock):
        mock_datetime.return_value = datetime(2024, 11, 26, 20, 1)
        io = IntelligentOffice()
        io.manage_blinds_based_on_time()
        self.assertFalse(io.blinds_open)


