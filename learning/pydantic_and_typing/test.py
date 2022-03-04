from ast import Dict, List
from decimal import Decimal

from pydantic import BaseModel
from pyparsing import Literal


class VacancyData(BaseModel):
    job_start_time: int
    link: str
    company: str
    resource: str
    trigger_method: str
    # errors: List[str] = []


class VacancyExtendedData(BaseModel):
    experience: str = ""
    eng_level: str = ""
    seniority: str = ""
    vacancy_title: str = ""
    primary_skill: str = ""
    # additional_skills: List[str] = []
    # optional_requirements: List[str] = []
    # errors: List[str] = []


class CompanyStatistics(BaseModel):
    links_count: int
    parsed_links_count: int
    time: Decimal


class Statistic(BaseModel):
    time: Decimal = 0
    trigger_method: str
    job_start_time: int
    companies: dict = {}


statistic = Statistic(trigger_method="self._trigger_method", job_start_time=12312).dict()
print(statistic)

def a(t: float):
    t["time"] += 0.2

def b(t: float):
    t["time"] += 1.3

t = {"time": 0.0}
a(t)
b(t)
print(t)
