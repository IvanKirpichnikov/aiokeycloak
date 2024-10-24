from __future__ import annotations

from dataclasses import dataclass

from aiokeycloak.types.base import FromResponse, KeycloakType


class Success(KeycloakType):
    @classmethod
    def from_response(
        cls,
        data: FromResponse,
    ) -> Success:
        return cls()


@dataclass(frozen=True, slots=True)
class Raw(KeycloakType):
    data: FromResponse

    @classmethod
    def from_response(
        cls,
        data: FromResponse,
    ) -> Raw:
        return cls(data)
