from dataclasses import dataclass
from enum import Enum


class BoxStatus(str, Enum):
    UNKNOWN = "UNKNOWN"
    DETECTED = "DETECTED"
    MEASURED = "MEASURED"
    ON_CONVEYOR = "ON_CONVEYOR"
    READY_FOR_PICK = "READY_FOR_PICK"
    PICKING = "PICKING"
    IN_TRANSIT = "IN_TRANSIT"
    PLACED = "PLACED"
    BUFFERED = "BUFFERED"
    REJECTED = "REJECTED"
    FAILED = "FAILED"


@dataclass(frozen=True)
class Size3D:
    x: float
    y: float
    z: float


@dataclass(frozen=True)
class Pose3D:
    frame_id: str
    x: float
    y: float
    z: float
    roll: float = 0.0
    pitch: float = 0.0
    yaw: float = 0.0


@dataclass(frozen=True)
class BoxState:
    box_id: str
    sku_id: str
    size: Size3D
    weight_kg: float
    pose: Pose3D
    allowed_yaws_rad: tuple[float, ...]
    status: BoxStatus
    confidence: float
    stamp_sec: float
    source: str


@dataclass(frozen=True)
class PlacedBox:
    box_id: str
    sku_id: str
    size: Size3D
    weight_kg: float
    pose: Pose3D


@dataclass(frozen=True)
class PalletState:
    pallet_id: str
    size: Size3D
    boxes: tuple[PlacedBox, ...]


@dataclass(frozen=True)
class InventoryState:
    tracked_boxes: dict[str, BoxState]
    remaining_by_sku: dict[str, int]


@dataclass(frozen=True)
class SystemState:
    state_version: int
    stamp_sec: float
    pallet: PalletState
    inventory: InventoryState
