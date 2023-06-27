import unittest
from pii_scan import show_aggie_pride, analyze_text
from presidio_analyzer import RecognizerResult


class TestPIIScan(unittest.TestCase):
    def test_aggie_pride(self):
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())

    def test_show_supported_entities(self):
        # test the show_supported_entities function
        # https://microsoft.github.io/presidio/supported_entities/
        results = analyze_text('This is a test', show_supported=True)
        print(results)
        self.assertTrue(True)

    def test_uuid(self):
        # test a valid UUID for detection
        results = analyze_text('This is a UUID: 123e4567-e89b-12d3-a456-42665234000c')
        self.assertIn('UUID', str(results))

        # test some uppercase letters
        results = analyze_text('This is a UUID: 123E4567-e89B-12d3-a456-4266523400FF')
        self.assertIn('UUID', str(results))

        # test an invalid UUID for detection
        results = analyze_text('This is not a UUID: 123e4567-e89b-12d3-a456-42665234000')
        self.assertNotIn('UUID', str(results))

    def test_political_group_detection(self):
        # test a valid political group
        results = analyze_text('I am a Democrat')
        self.assertIn('NRP', str(results))

        results = analyze_text('I am a Republican')
        self.assertIn('NRP', str(results))

        results = analyze_text('This is a democracy')
        self.assertNotIn('NRP', str(results))

    def test_social_security_detection(self):
            # test a valid social security number 
        results = analyze_text('This is a SSN: 121-35-1146')
        self.assertIn('US_SSN', str(results))

        results = analyze_text('This is a SSN: 646-13-6685')
        self.assertIn('US_SSN' , str(results))

        results = analyze_text('This is a SSN: 325-46-2435')
        self.assertIn('US_SSN' , str(results))

        results = analyze_text('This is a SSN: 413-78-3543')
        self.assertIn('US_SSN' , str(results))

        results = analyze_text('This is a SSN: 856-45-6789')
        self.assertIn('US_SSN' , str(results))

        results = analyze_text('This is a SSN: 227-58-8812')
        self.assertIn('US_SSN' , str(results))

        results = analyze_text('This is a SSN: 598-92-9968')
        self.assertIn('US_SSN' , str(results))

        results = analyze_text('This is a SSN: 734-41-1135')
        self.assertIn('US_SSN' , str(results))

        results = analyze_text('This is not a SSN: 947-603-4211')
        self.assertNotIn('US_SSN' , str(results))

        results = analyze_text('This is not a SSN: 1256547632')
        self.assertNotIn('US_SSN' , str(results))

        results = analyze_text('This is not a SSN: 000,46,8789')
        self.assertNotIn('US_SSN' , str(results))

        results = analyze_text('This is not a SSN: #ABCDEFAB')
        self.assertNotIn('US_SSN' , str(results))

        results = analyze_text('This is not a SSN: +1233456689')
        self.assertNotIn('US_SSN' , str(results))

if __name__ == '__main__':
    unittest.main()
