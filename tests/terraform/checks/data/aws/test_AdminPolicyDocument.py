import unittest
from pathlib import Path

from checkov.runner_filter import RunnerFilter
from checkov.terraform.checks.data.aws.AdminPolicyDocument import check
from checkov.terraform.runner import Runner


class TestAdminPolicyDocument(unittest.TestCase):
    def test(self):
        test_files_dir = Path(__file__).parent / "example_AdminPolicyDocument"

        report = Runner().run(root_folder=test_files_dir, runner_filter=RunnerFilter(checks=[check.id]))
        summary = report.get_summary()

        passing_resources = {
            "aws_iam_policy_document.list",
            "aws_iam_policy_document.pass",
        }
        failing_resources = {
            "aws_iam_policy_document.fail",
            "aws_iam_policy_document.no_effect",
        }

        passed_check_resources = set([c.resource for c in report.passed_checks])
        failed_check_resources = set([c.resource for c in report.failed_checks])

        self.assertEqual(summary["passed"], 2)
        self.assertEqual(summary["failed"], 2)
        self.assertEqual(summary["skipped"], 0)
        self.assertEqual(summary["parsing_errors"], 0)

        self.assertEqual(passing_resources, passed_check_resources)
        self.assertEqual(failing_resources, failed_check_resources)


if __name__ == "__main__":
    unittest.main()
