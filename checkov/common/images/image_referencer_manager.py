from __future__ import annotations

from checkov.common.images.image_referencer_provider import Provider

from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from checkov.common.images.image_referencer import Image


class ImageReferencerManager:
    provider: Provider = None

    def __init__(self, workflow_config: dict[str, Any], file_path: str):
        self.workflow_config = workflow_config
        self.file_path = file_path

    def extract_images_from_workflow(self) -> list[Image]:
        images: list[Image] = self.provider.extract_images_from_workflow()
        return images
