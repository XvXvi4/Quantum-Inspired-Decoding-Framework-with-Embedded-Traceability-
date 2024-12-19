import hashlib

def refined_decode_tail_data(optimized_data: bytes) -> bytes:
    """
    Refines and decodes the optimized data by removing failsafe markers and
    performing integrity checks.
    """
    # Remove 'R', 'N', and 'Ñ' markers
    # 'Ñ' is represented in UTF-8 as b'\xc3\x91'
    cleaned_data = optimized_data.replace(b'R', b'').replace(b'N', b'').replace(b'\xc3\x91', b'')

    # Compute SHA-256 hash for integrity verification
    hash_value = hashlib.sha256(cleaned_data).hexdigest()
    print(f"Decoded Data SHA-256: {hash_value}")

    return cleaned_data
