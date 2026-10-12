import unittest

import asn1tools_ext


class Asn1ToolsAliasTest(unittest.TestCase):
    def test_package(self):
        import asn1tools

        self.assertIs(asn1tools, asn1tools_ext)
        self.assertIs(asn1tools.compile_string, asn1tools_ext.compile_string)

    def test_submodules(self):
        import asn1tools.codecs.per
        import asn1tools_ext.codecs.per
        from asn1tools.codecs import utc_time_to_datetime
        from asn1tools.compiler import Specification
        from asn1tools.errors import DecodeError

        self.assertIs(asn1tools.codecs.per, asn1tools_ext.codecs.per)
        self.assertIs(utc_time_to_datetime, asn1tools_ext.codecs.utc_time_to_datetime)
        self.assertIs(Specification, asn1tools_ext.compiler.Specification)
        self.assertIs(DecodeError, asn1tools_ext.errors.DecodeError)

    def test_encode_decode(self):
        import asn1tools

        foo = asn1tools.compile_string(
            "Foo DEFINITIONS AUTOMATIC TAGS ::= BEGIN A ::= BOOLEAN END"
        )

        self.assertEqual(foo.encode("A", True), b"\x01\x01\xff")

        with self.assertRaises(asn1tools.DecodeError):
            foo.decode("A", b"")
