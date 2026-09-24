import math


def _to_float(value):
    try:
        return float(value)
    except (TypeError, ValueError, OverflowError):
        return None


def estimate_capacity(
    area_km2,
    net_thickness_m,
    porosity_fraction,
    co2_density_kg_m3,
    storage_efficiency_factor,
):
    area = _to_float(area_km2)
    thickness = _to_float(net_thickness_m)
    porosity = _to_float(porosity_fraction)
    density = _to_float(co2_density_kg_m3)
    efficiency = _to_float(storage_efficiency_factor)

    errors = []

    if area is None or not math.isfinite(area) or area <= 0:
        errors.append("Area must be a positive finite number in km².")

    if thickness is None or not math.isfinite(thickness) or thickness <= 0:
        errors.append("Net thickness must be a positive finite number in meters.")

    if porosity is None or not math.isfinite(porosity) or porosity < 0.0 or porosity > 0.5:
        errors.append("Porosity must be between 0.0 and 0.5.")

    if density is None or not math.isfinite(density) or density <= 0:
        errors.append("CO2 density must be a positive finite number in kg/m³.")

    if efficiency is None or not math.isfinite(efficiency) or efficiency < 0.01 or efficiency > 0.10:
        errors.append("Storage efficiency factor must be between 0.01 and 0.10.")

    if errors:
        return {
            "valid": False,
            "errors": errors,
            "capacity_mt": None,
            "category": "Invalid",
            "color": "#dc3545",
            "text_color": "#ffffff",
        }

    area_m2 = area * 1_000_000.0
    pore_volume_m3 = area_m2 * thickness * porosity
    mass_kg = pore_volume_m3 * density * efficiency
    capacity_mt = mass_kg / 1_000_000_000.0

    if not math.isfinite(capacity_mt):
        return {
            "valid": False,
            "errors": ["Computed capacity is too large to represent."],
            "capacity_mt": None,
            "category": "Invalid",
            "color": "#dc3545",
            "text_color": "#ffffff",
        }

    if capacity_mt < 10:
        category = "Small"
        color = "#dc3545"
        text_color = "#ffffff"
    elif capacity_mt <= 100:
        category = "Medium"
        color = "#ffc107"
        text_color = "#111111"
    else:
        category = "Large"
        color = "#28a745"
        text_color = "#ffffff"

    return {
        "valid": True,
        "capacity_mt": capacity_mt,
        "category": category,
        "color": color,
        "text_color": text_color,
        "pore_volume_m3": pore_volume_m3,
        "mass_kg": mass_kg,
    }


def format_capacity_html(result):
    if isinstance(result, dict) and result.get("valid"):
        capacity = result.get("capacity_mt", 0.0)
        return (
            '<div style="font-size:32px; font-weight:bold; text-align:center; '
            'margin-bottom:12px; color:#111111;">'
            f"Estimated CO2 storage capacity: {capacity:.2f} Mt"
            "</div>"
        )

    return (
        '<div style="font-size:28px; font-weight:bold; text-align:center; '
        'margin-bottom:12px; color:#721c24;">'
        "Estimated CO2 storage capacity: —"
        "</div>"
    )


def format_category_html(result):
    if isinstance(result, dict) and result.get("valid"):
        threshold_map = {
            "Small": "< 10 Mt",
            "Medium": "10-100 Mt",
            "Large": "> 100 Mt",
        }
        category = result.get("category", "")
        threshold = threshold_map.get(category, "")
        color = result.get("color", "#dc3545")
        text_color = result.get("text_color", "#ffffff")

        return (
            '<div style="background-color:'
            + color
            + "; color:"
            + text_color
            + "; padding:16px; border-radius:8px; font-size:20px; font-weight:bold; "
            'text-align:center; border:1px solid rgba(0,0,0,0.1);">'
            + "Storage potential: "
            + category
            + " ("
            + threshold
            + ")"
            + "</div>"
        )

    errors = result.get("errors", ["Invalid input."]) if isinstance(result, dict) else ["Invalid input."]
    message = "<br>".join(f"&bull; {error}" for error in errors)

    return (
        '<div style="background-color:#f8d7da; color:#721c24; padding:16px; '
        'border-radius:8px; font-size:16px; text-align:left; border:1px solid #f5c6cb;">'
        "<strong>Invalid input</strong><br>"
        + message
        + "</div>"
    )
