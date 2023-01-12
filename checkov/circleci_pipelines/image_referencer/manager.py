from __future__ import annotations
from typing import Any

from checkov.circleci_pipelines.image_referencer.provider import CircleCIProvider
from checkov.common.images.image_referencer_manager import ImageReferencerManager


class CircleCIImageReferencerManager(ImageReferencerManager):
    __slots__ = ("workflow_config", "file_path", "provider")

    def __init__(self, workflow_config: dict[str, Any], file_path: str) -> None:
        super().__init__(workflow_config, file_path)
        self.provider = CircleCIProvider(workflow_config=self.workflow_config, file_path=self.file_path)

