from faker import Faker
from faker.providers import DynamicProvider
from input.area.index import Area

fake = Faker('zh_CN')


area = Area()
area_district_list = area.export_district_list()

area_district_provider = DynamicProvider(
    provider_name="area_district",
    elements=area_district_list
)

fake.add_provider(area_district_provider)


def mock_area():
    """模拟地区，先随机出一个地区，再反向确定市和省

    Returns:
        _type_: _description_
    """

    area_district_or_county = fake.area_district()
    area_city = area.export_city(area_district_or_county)
    area_province = area.export_province()

    return {
        "province": area_province,
        "city": area_city,
        "district_or_county": area_district_or_county,
    }
