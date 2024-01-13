from typing import Any, Dict, List, Tuple, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UploadArrayOfFilesInObjectTestsUploadPostBody")


@_attrs_define
class UploadArrayOfFilesInObjectTestsUploadPostBody:
    """ """

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    def to_multipart(self) -> List[Tuple[str, Any]]:
        field_list: List[Tuple[str, Any]] = []

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )

        field_list += list(field_dict.items())

        return field_list

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        upload_array_of_files_in_object_tests_upload_post_body = cls()

        upload_array_of_files_in_object_tests_upload_post_body.additional_properties = d
        return upload_array_of_files_in_object_tests_upload_post_body

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
