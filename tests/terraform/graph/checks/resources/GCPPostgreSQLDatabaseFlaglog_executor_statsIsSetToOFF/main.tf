#case1 - PASS
resource "google_sql_database_instance" "postgresql-instance-ok-1" {
  name    = "postgresql-instance-ok-1"
  database_version = "POSTGRES_14"
  settings {
    database_flags {
      name  = "log_executor_stats"
      value = "off"
    }
    tier = "db-f1-micro"
  }
  deletion_protection = false
}

#case2 - PASS
resource "google_sql_database_instance" "postgresql-instance-ok-2" {
  name    = "postgresql-instance-ok-2"
  database_version = "POSTGRES_14"
  settings {
    tier = "db-f1-micro"
  }
  deletion_protection = false
}

#case3 - FAIL
resource "google_sql_database_instance" "postgresql-instance-not-ok-1" {
  name    = "postgresql-instance-not-ok-1"
  database_version = "POSTGRES_14"
  settings {
    database_flags {
      name  = "log_executor_stats"
      value = "on"
    }
    tier = "db-f1-micro"
  }
  deletion_protection = false
}