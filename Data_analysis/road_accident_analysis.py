"""
Road accident dataset: temporal analysis and deeper insights.
Appends sections 3-4 to road_accident_summary.md and saves CSVs/plots to Data_analysis/.
Run after road_accident_data_report.py.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

BASE = Path(__file__).resolve().parent
CSV_PATH = BASE / "road_accident_dataset.csv"
SUMMARY_PATH = BASE / "road_accident_summary.md"


def load_data():
    return pd.read_csv(CSV_PATH)


def section3_temporal(df: pd.DataFrame) -> str:
    """Phase 3: time of day, day of week, month, year."""
    lines = ["## 3. Temporal findings\n\n"]

    # Time of day
    tod = df.groupby("Time of Day").agg(
        accidents=("Time of Day", "count"),
        fatalities=("Number of Fatalities", "sum"),
    ).reindex(["Morning", "Afternoon", "Evening", "Night"]).fillna(0)
    tod.to_csv(BASE / "temporal_time_of_day.csv")
    lines.append("**By time of day:**\n\n```\n")
    lines.append(tod.to_string() + "\n```\n\n")

    # Day of week
    dow_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    dow = df.groupby("Day of Week").agg(
        accidents=("Day of Week", "count"),
        fatalities=("Number of Fatalities", "sum"),
    ).reindex(dow_order).fillna(0)
    dow.to_csv(BASE / "temporal_day_of_week.csv")
    lines.append("**By day of week:**\n\n```\n")
    lines.append(dow.to_string() + "\n```\n\n")

    # Month
    month_order = ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December"]
    mon = df.groupby("Month").agg(
        accidents=("Month", "count"),
        fatalities=("Number of Fatalities", "sum"),
    ).reindex(month_order).fillna(0)
    mon.to_csv(BASE / "temporal_month.csv")
    lines.append("**By month:**\n\n```\n")
    lines.append(mon.to_string() + "\n```\n\n")

    # Year
    yr = df.groupby("Year").agg(
        accidents=("Year", "count"),
        fatalities=("Number of Fatalities", "sum"),
    ).sort_index()
    yr.to_csv(BASE / "temporal_year.csv")
    lines.append("**By year:**\n\n```\n")
    lines.append(yr.to_string() + "\n```\n\n")

    # Plots
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    tod.plot(y="accidents", kind="bar", ax=axes[0, 0], legend=False)
    axes[0, 0].set_title("Accidents by time of day")
    axes[0, 0].tick_params(axis="x", rotation=45)

    dow.plot(y="accidents", kind="bar", ax=axes[0, 1], legend=False)
    axes[0, 1].set_title("Accidents by day of week")
    axes[0, 1].tick_params(axis="x", rotation=45)

    mon.plot(y="accidents", kind="bar", ax=axes[1, 0], legend=False)
    axes[1, 0].set_title("Accidents by month")
    axes[1, 0].tick_params(axis="x", rotation=45)

    yr.plot(ax=axes[1, 1], legend=False)
    axes[1, 1].set_title("Accidents and fatalities by year")
    axes[1, 1].set_ylabel("Count")
    plt.tight_layout()
    plt.savefig(BASE / "temporal_patterns.svg", format="svg")
    plt.close()

    lines.append("Plots saved: `temporal_patterns.svg`.\n\n")
    return "".join(lines)


def section4_deeper_insights(df: pd.DataFrame) -> str:
    """Phase 4: exploratory questions."""
    lines = ["## 4. Deeper insights\n\n"]

    # Severity vs cause
    sev_cause = pd.crosstab(df["Accident Cause"], df["Accident Severity"])
    sev_cause.to_csv(BASE / "insight_severity_by_cause.csv")
    lines.append("### 4.1 Accident severity by cause\n\n```\n")
    lines.append(sev_cause.to_string() + "\n```\n\n")

    # Urban vs rural
    urb = df.groupby("Urban/Rural").agg(
        accidents=("Urban/Rural", "count"),
        total_fatalities=("Number of Fatalities", "sum"),
        avg_injuries=("Number of Injuries", "mean"),
    ).round(2)
    urb["fatalities_per_accident"] = (urb["total_fatalities"] / urb["accidents"]).round(4)
    urb.to_csv(BASE / "insight_urban_rural.csv")
    lines.append("### 4.2 Urban vs rural\n\n```\n")
    lines.append(urb.to_string() + "\n```\n\n")

    # Fatalities vs driver age
    age_fat = df.groupby("Driver Age Group").agg(
        accidents=("Driver Age Group", "count"),
        total_fatalities=("Number of Fatalities", "sum"),
    )
    age_fat["fatalities_per_accident"] = (age_fat["total_fatalities"] / age_fat["accidents"]).round(4)
    age_fat = age_fat.reindex(["<18", "18-25", "26-40", "41-60", "61+"])
    age_fat.to_csv(BASE / "insight_fatalities_by_age.csv")
    lines.append("### 4.3 Fatalities by driver age group\n\n```\n")
    lines.append(age_fat.to_string() + "\n```\n\n")

    # Severity vs emergency response time
    resp = df.groupby("Accident Severity")["Emergency Response Time"].agg(["mean", "median", "count"]).round(2)
    resp.to_csv(BASE / "insight_response_by_severity.csv")
    lines.append("### 4.4 Emergency response time by severity\n\n```\n")
    lines.append(resp.to_string() + "\n```\n\n")

    # Plot: severity by cause (stacked or top causes)
    cause_totals = df.groupby("Accident Cause")["Number of Fatalities"].sum().sort_values(ascending=False).head(8)
    fig, ax = plt.subplots(figsize=(8, 5))
    cause_totals.plot(kind="barh", ax=ax)
    ax.set_title("Total fatalities by accident cause (top 8)")
    ax.set_xlabel("Fatalities")
    plt.tight_layout()
    plt.savefig(BASE / "insight_fatalities_by_cause.svg", format="svg")
    plt.close()

    lines.append("Plot saved: `insight_fatalities_by_cause.svg`.\n\n")
    return "".join(lines)


def main():
    df = load_data()
    part3 = section3_temporal(df)
    part4 = section4_deeper_insights(df)
    with open(SUMMARY_PATH, "a") as f:
        f.write(part3)
        f.write(part4)
    print(f"Appended sections 3–4 to {SUMMARY_PATH}. CSVs and SVGs in {BASE}.")


if __name__ == "__main__":
    main()
