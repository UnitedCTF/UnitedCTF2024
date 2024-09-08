#!/bin/bash


files=(
    "maintenance/urgent/unitedCTF2024/report_2024.txt"
    "maintenance/archives/2024/inspection_report_2024.txt"
    "maintenance/repair_carousel.txt"
    "maintenance/archives/2023/inspection_report_2023.txt"
    "maintenance/archives/2023/preventive_maintenance_2023.txt"
    "maintenance/urgent/roller_coaster_issue.txt"
    "maintenance/inspection_safety_harnesses.txt"
    "maintenance/maintenance_water_ride.txt"
    "maintenance/reparation_roller_coaster.txt"
    "maintenance/archives/2022/rapport_inspection_2022.txt"
    "maintenance/archives/2022/rapport_maintenance_preventive_2022.txt"
    "maintenance/urgent/swing_ride_issue.txt"
    "maintenance/inspection_cables.txt"
    "maintenance/maintenance_track_replacement.txt"
    "maintenance/reparation_ferris_wheel_motor.txt"
    "maintenance/archives/2021/inspection_report_2021.txt"
    "maintenance/archives/2021/preventive_maintenance_2021.txt"
    "maintenance/urgent/water_ride_leak.txt"
    "maintenance/inspection_brakes.txt"
    "maintenance/maintenance_hydraulics.txt"
    "maintenance/reparation_gondolas.txt"
    "maintenance/archives/2020/inspection_report_2020.txt"
    "maintenance/archives/2020/preventive_maintenance_2020.txt"
    "maintenance/urgent/electrical_issue.txt"
    "maintenance/inspection_ride_seats.txt"
    "maintenance/maintenance_control_system.txt"
    "maintenance/reparation_wheel_axles.txt"
    "maintenance/archives/2019/inspection_report_2019.txt"
    "maintenance/archives/2019/preventive_maintenance_2019.txt"
    "maintenance/urgent/ride_control_issue.txt"
    "maintenance/inspection_ride_tracks.txt"
    "maintenance/maintenance_gear_systems.txt"
    "maintenance/reparation_support_structures.txt"
    "maintenance/archives/2018/inspection_report_2018.txt"
    "maintenance/archives/2018/preventive_maintenance_2018.txt"
    "maintenance/urgent/structural_issue.txt"
    "maintenance/inspection_cable_tension.txt"
    "maintenance/maintenance_safety_systems.txt"
    "maintenance/reparation_control_panel.txt"
    "maintenance/archives/2017/inspection_report_2017.txt"
    "maintenance/archives/2017/preventive_maintenance_2017.txt"
    "maintenance/urgent/control_system_failure.txt"
    "maintenance/inspection_support_columns.txt"
    "maintenance/maintenance_safety_brakes.txt"
    "maintenance/reparation_hydraulic_pumps.txt"
    "maintenance/archives/2016/inspection_report_2016.txt"
    "maintenance/archives/2016/preventive_maintenance_2016.txt"
    "maintenance/urgent/ride_seatbelt_issue.txt"
    "maintenance/inspection_wiring.txt"
    "maintenance/maintenance_water_pump.txt"
    "maintenance/reparation_hydraulic_systems.txt"
    "maintenance/archives/2015/inspection_report_2015.txt"
    "maintenance/archives/2015/preventive_maintenance_2015.txt"
    "maintenance/urgent/power_failure.txt"
    "maintenance/inspection_gear_alignment.txt"
    "maintenance/maintenance_lubrication.txt"
    "maintenance/reparation_seating_structure.txt"
    "maintenance/archives/2014/inspection_report_2014.txt"
    "maintenance/archives/2014/preventive_maintenance_2014.txt"
    "maintenance/urgent/safety_harness_issue.txt"
    "maintenance/inspection_motor_performance.txt"
    "maintenance/maintenance_bearing_replacement.txt"
    "maintenance/reparation_control_system.txt"
    "maintenance/archives/2013/inspection_report_2013.txt"
    "maintenance/archives/2013/preventive_maintenance_2013.txt"
    "maintenance/urgent/ride_overheating_issue.txt"
    "maintenance/inspection_safety_protocols.txt"
    "maintenance/maintenance_electrical_system.txt"
    "maintenance/reparation_support_beams.txt"
    "maintenance/archives/2012/inspection_report_2012.txt"
    "maintenance/archives/2012/preventive_maintenance_2012.txt"
    "maintenance/urgent/ride_speed_control_issue.txt"
    "maintenance/inspection_safety_mechanisms.txt"
    "maintenance/maintenance_ride_cushions.txt"
    "maintenance/reparation_power_supply.txt"
    "maintenance/archives/2011/inspection_report_2011.txt"
    "maintenance/archives/2011/preventive_maintenance_2011.txt"
    "maintenance/urgent/control_system_overload.txt"
    "maintenance/inspection_safety_nets.txt"
    "maintenance/maintenance_supports.txt"
    "maintenance/reparation_control_room.txt"
    "maintenance/archives/2010/inspection_report_2010.txt"
    "maintenance/archives/2010/preventive_maintenance_2010.txt"
    "maintenance/urgent/ride_gearbox_issue.txt"
    "maintenance/inspection_emergency_stops.txt"
    "maintenance/maintenance_safety_harnesses.txt"
    "maintenance/reparation_ride_controls.txt"
)


for file in "${files[@]}"; do
    dir=$(dirname "$file")
    mkdir -p "$dir"
done

generate_random_content() {
    local size=$((RANDOM % 100 + 10))
    base64 /dev/urandom | head -c $size
}

for file in "${files[@]}"; do
    echo "$(generate_random_content)" > "$file"
done
