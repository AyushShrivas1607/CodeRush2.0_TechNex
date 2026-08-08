class SpacecraftDigitalTwin:
    def __init__(self):
        self.battery_level = 100.0  # percentage
        self.internal_temp = 22.5   # Celsius
        self.solar_panel_status = "HEALTHY"

    def step_simulation(self, inject_fault=False):
        """Simulates one telemetry tick with optional fault injection."""
        if inject_fault:
            self.battery_level -= 3.5
            self.internal_temp += 8.0  # Thermal excursion
            self.solar_panel_status = "DEGRADED_OBSTRUCTED"
        else:
            self.battery_level -= 0.5
            self.internal_temp = 22.5
            self.solar_panel_status = "HEALTHY"
            
        return {
            "battery": max(0.0, self.battery_level),
            "temperature": self.internal_temp,
            "status": self.solar_panel_status
        }