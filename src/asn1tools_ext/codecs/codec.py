class Codec:
    """
    Base interface type for codecs.
    """

    @staticmethod
    def compile_dict(specification, numeric_enums=False):
        raise NotImplementedError("Subclasses must implement this method.")

    @staticmethod
    def decode_full_length(data):
        raise NotImplementedError("Subclasses must implement this method.")
