from dataclasses import dataclass, field
from typing import Optional, List, Dict


@dataclass
class Detection:
    name: str
    category: str
    confidence: int
    version: Optional[str] = None
    evidence: List[str] = field(default_factory=list)

    def __repr__(self):
        v = f" v{self.version}" if self.version else ""
        return f"<{self.name}{v} ({self.confidence}%)>"


@dataclass
class ScanResult:
    url: str
    status_code: int = 0
    detections: List[Detection] = field(default_factory=list)
    headers: Dict[str, str] = field(default_factory=dict)
    cookies: List[str] = field(default_factory=list)
    security_headers: Dict[str, bool] = field(default_factory=dict)
    technologies: Dict[str, List[str]] = field(default_factory=dict)

    @property
    def count(self) -> int:
        return len([d for d in self.detections if d.category != "security"])

    def has(self, name: str) -> bool:
        return any(d.name.lower() == name.lower() for d in self.detections)

    def by_category(self, category: str) -> List[Detection]:
        return [d for d in self.detections if d.category == category]
