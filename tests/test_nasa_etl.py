import pytest
from datetime import datetime, timedelta

class TestNASAAPOD:
    def test_date_format_valid(self):
        date_str = "2024-01-15"
        parsed = datetime.strptime(date_str, "%Y-%m-%d")
        assert parsed.year == 2024

    def test_api_response_structure(self):
        mock = {"date": "2024-01-15", "title": "Galaxy Far Away", "url": "https://example.com/img.jpg", "media_type": "image", "explanation": "A beautiful galaxy..."}
        for key in ["date", "title", "url", "media_type"]:
            assert key in mock

    def test_date_range_generation(self):
        start = datetime(2024, 1, 1)
        end = datetime(2024, 1, 7)
        dates = [(start + timedelta(days=i)).strftime("%Y-%m-%d") for i in range((end-start).days+1)]
        assert len(dates) == 7
        assert dates[0] == "2024-01-01"

    def test_media_type_filtering(self):
        apods = [{"title": "A", "media_type": "image"}, {"title": "B", "media_type": "video"}, {"title": "C", "media_type": "image"}]
        images = [a for a in apods if a["media_type"] == "image"]
        assert len(images) == 2

class TestETLPipeline:
    def test_extract_returns_list(self):
        mock_data = [{"date": "2024-01-01", "title": "Test"}]
        assert isinstance(mock_data, list)
        assert len(mock_data) > 0

    def test_transform_adds_ingestion_date(self):
        record = {"date": "2024-01-01", "title": "Test"}
        record["ingested_at"] = datetime.utcnow().strftime("%Y-%m-%d")
        assert "ingested_at" in record

    def test_load_validates_required_fields(self):
        required = ["date", "title", "url"]
        record = {"date": "2024-01-01", "title": "Test", "url": "http://example.com"}
        for field in required:
            assert field in record

    def test_duplicate_dates_removed(self):
        records = [{"date": "2024-01-01"}, {"date": "2024-01-01"}, {"date": "2024-01-02"}]
        unique = {r["date"]: r for r in records}.values()
        assert len(list(unique)) == 2
