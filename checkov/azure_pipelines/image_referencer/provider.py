from __future__ import annotations

from typing import Any

from checkov.common.images.image_referencer import Image
from checkov.azure_pipelines.common.resource_id_utils import generate_resource_key_recursive
from checkov.common.images.image_referencer_provider import Provider


class AzurePipelinesProvider(Provider):

    def __init__(self, workflow_config: dict[str, Any], file_path: str):
        super().__init__(workflow_config, file_path)
        self.supported_keys = "container"

    def extract_images_from_workflow(self) -> list[Image]:
        images = self.extract_images_from_dict(self.workflow_config)
        return images

    def extract_images_from_list(self, objects_list: list[dict[str, Any]]) -> list[Image]:
        images = []
        for job in objects_list:
            if isinstance(job, dict):
                images.extend(self.extract_images_from_dict(job))
            if isinstance(job, list):
                images.extend(self.extract_images_from_list(job))
        return images

    def extract_images_from_dict(self, job: dict[str, Any]) -> list[Image]:
        images = []
        start_line, end_line = AzurePipelinesProvider._get_start_end_lines(job)
        for key, sub_job in job.items():
            if key == self.supported_keys:
                images.append(self.crete_image(sub_job, start_line, end_line))
            elif isinstance(sub_job, dict):
                images.extend(self.extract_images_from_dict(sub_job))
            elif isinstance(sub_job, list):
                images.extend(self.extract_images_from_list(sub_job))
        return images

    def crete_image(self, container: dict[str, Any] | str, start_line: int, end_line: int) -> Image:
        image_name = ''
        if isinstance(container, str):
            image_name = container
        elif isinstance(container, dict):
            if 'image' in container:
                image_name = container['image']
        return Image(
            file_path=self.file_path,
            name=image_name,
            start_line=start_line,
            end_line=end_line,
            related_resource_id=generate_resource_key_recursive(file_conf=self.workflow_config,
                                                                resource_key='',
                                                                start_line=start_line,
                                                                end_line=end_line))
