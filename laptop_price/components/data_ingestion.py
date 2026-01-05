from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

from laptop_price.logger import get_logger
from laptop_price.exception import PricePredictorException
from laptop_price.config import ARTIFACTS_DIR, MYSQL
from laptop_price.entity.artifact_entity import DataIngestionArtifact

logger = get_logger(__name__)


def ingest_data() -> DataIngestionArtifact:
    """
    Ingest data from MySQL database and store it in artifacts/raw/
    """

    try:
        logger.info("Starting MySQL data ingestion")

        user = MYSQL["user"]
        password = MYSQL["password"]
        host = MYSQL["host"]
        port = MYSQL["port"]
        database = MYSQL["database"]
        table = MYSQL["table"]

        # ✅ MySQL connection
        engine = create_engine(
            f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
        )

        # ✅ Read table
        df = pd.read_sql_table(table, con=engine)
        logger.info(f"Data loaded from MySQL with shape {df.shape}")

        # ✅ Save to artifacts/raw
        raw_dir = ARTIFACTS_DIR / "raw"
        raw_dir.mkdir(parents=True, exist_ok=True)

        raw_data_path = raw_dir / "laptop_data.csv"
        df.to_csv(raw_data_path, index=False)

        logger.info(f"Raw data saved at {raw_data_path}")

        return DataIngestionArtifact(
            raw_data_path=raw_data_path
        )

    except Exception as e:
        logger.exception("Data ingestion failed")
        raise PricePredictorException(f"Data ingestion failed: {e}")
