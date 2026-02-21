import json
import os

def get_recommendations(score, profile, arch):
    """
    Suggests Linux distributions based on score, profile, and architecture.
    """
    path = os.path.join(os.path.dirname(__file__), 'profiles.json')
    with open(path, 'r', encoding='utf-8') as f:
        profiles = json.load(f)

    if '32' in arch:
        return profiles.get('legacy_32bits', [])

    if profile == "High-end":
        return profiles.get('high', [])
    elif profile == "Mid-range":
        return profiles.get('mid', [])
    else:
        return profiles.get('low', [])

if __name__ == "__main__":
    print(get_recommendations(58, "Mid-range", "64-bit"))
