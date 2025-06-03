# tests/fixtures/test_data.py
"""
Test data fixtures using factory_boy for generating realistic test data.

This approach is better than hard-coded mocks because:
- Data looks realistic
- Easy to generate variations
- Reduces test brittleness
- Follows DRY principles
"""

import uuid
from datetime import datetime

import factory
from faker import Faker

fake = Faker()


class OrgFactory(factory.Factory):
    """Factory for generating organisation data"""

    class Meta:
        model = dict

    id = factory.LazyFunction(lambda: str(uuid.uuid4()))
    name = factory.Faker("company")
    created_time = factory.LazyFunction(lambda: int(datetime.now().timestamp()))
    modified_time = factory.LazyFunction(lambda: int(datetime.now().timestamp()))
    orggroup_ids = factory.List([])
    alarmtemplate_id = None
    allow_mist = True
    session_expiry = 1440


class SiteFactory(factory.Factory):
    """Factory for generating site data"""

    class Meta:
        model = dict

    id = factory.LazyFunction(lambda: str(uuid.uuid4()))
    name = factory.Faker("word")
    org_id = factory.LazyFunction(lambda: str(uuid.uuid4()))
    created_time = factory.LazyFunction(lambda: int(datetime.now().timestamp()))
    modified_time = factory.LazyFunction(lambda: int(datetime.now().timestamp()))
    country_code = factory.Faker("country_code")
    timezone = factory.Faker("timezone")
    address = factory.Faker("address")


class DeviceFactory(factory.Factory):
    """Factory for generating device data"""

    class Meta:
        model = dict

    id = factory.LazyFunction(lambda: fake.hexify(text="^^^^^^^^^^^^", upper=False))
    mac = factory.LazyFunction(lambda: fake.hexify(text="^^^^^^^^^^^^", upper=False))
    model = factory.Iterator(["AP41", "AP43", "AP45", "EX2300", "SRX300"])
    type = factory.Iterator(["ap", "switch", "gateway"])
    name = factory.Faker("word")
    site_id = factory.LazyFunction(lambda: str(uuid.uuid4()))
    org_id = factory.LazyFunction(lambda: str(uuid.uuid4()))
    created_time = factory.LazyFunction(lambda: int(datetime.now().timestamp()))
    modified_time = factory.LazyFunction(lambda: int(datetime.now().timestamp()))
    serial = factory.LazyFunction(
        lambda: fake.pystr_format(
            string_format="???#########", letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        )
    )


class UserFactory(factory.Factory):
    """Factory for generating user data"""

    class Meta:
        model = dict

    id = factory.LazyFunction(lambda: str(uuid.uuid4()))
    email = factory.Faker("email")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    phone = factory.Faker("phone_number")
    two_factor_required = False
    two_factor_passed = True
    via_sso = False
    tags = factory.List([])

    @factory.post_generation
    def privileges(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            self["privileges"] = extracted
        else:
            # Default privileges
            self["privileges"] = [
                {
                    "scope": "org",
                    "role": "admin",
                    "org_id": str(uuid.uuid4()),
                    "name": fake.company(),
                }
            ]


class PrivilegeFactory(factory.Factory):
    """Factory for generating privilege data"""

    class Meta:
        model = dict

    scope = factory.Iterator(["org", "site", "msp"])
    role = factory.Iterator(["admin", "write", "read"])
    name = factory.Faker("company")

    @factory.lazy_attribute
    def org_id(self):
        if self.scope in ["org", "site"]:
            return str(uuid.uuid4())
        return None

    @factory.lazy_attribute
    def site_id(self):
        if self.scope == "site":
            return str(uuid.uuid4())
        return None

    @factory.lazy_attribute
    def msp_id(self):
        if self.scope == "msp":
            return str(uuid.uuid4())
        return None


# Commonly used test data combinations
SAMPLE_CLOUDS = [
    {"short": "APAC 01", "host": "api.ac5.mist.com", "cookies_ext": ".ac5"},
    {"short": "Europe 01", "host": "api.eu.mist.com", "cookies_ext": ".eu"},
    {"short": "Global 01", "host": "api.mist.com", "cookies_ext": ""},
    {"short": "Global 02", "host": "api.gc1.mist.com", "cookies_ext": ".gc1"},
]

SAMPLE_ERROR_RESPONSES = {
    400: {"detail": "Bad Request", "error": "invalid_request"},
    401: {"detail": "Unauthorized", "error": "invalid_credentials"},
    403: {"detail": "Forbidden", "error": "insufficient_privileges"},
    404: {"detail": "Not Found", "error": "resource_not_found"},
    429: {"detail": "Too Many Requests", "error": "rate_limit_exceeded"},
    500: {"detail": "Internal Server Error", "error": "server_error"},
}

SAMPLE_DEVICE_MODELS = [
    "AP12",
    "AP21",
    "AP32",
    "AP33",
    "AP41",
    "AP43",
    "AP45",
    "AP61",
    "AP63",
    "EX2300-24T",
    "EX2300-48T",
    "EX3400-24T",
    "EX3400-48T",
    "EX4300-48T",
    "SRX300",
    "SRX320",
    "SRX340",
    "SRX345",
    "SRX550",
]
