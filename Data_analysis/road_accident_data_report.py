"""
Road accident dataset: data structure report and geographic analysis.
Writes sections 1-2 to road_accident_summary.md and saves CSVs/plots to Data_analysis/.
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


def section1_data_structure(df: pd.DataFrame) -> str:
    """Phase 1: schema, quality, univariate summaries, cross-checks."""
    lines = ["# Road Accident Dataset — Summary Report\n", "## 1. Data structure report\n"]

    # Schema
    lines.append("### 1.1 Schema\n")
    lines.append(f"- **Rows:** {len(df):,}\n")
    lines.append(f"- **Columns:** {len(df.columns)}\n\n")
    lines.append("| Column | Dtype | Kind | Notes |\n|--------|--------|------|------|\n")

    categorical = [
        "Country", "Month", "Day of Week", "Time of Day", "Urban/Rural", "Road Type",
        "Weather Conditions", "Vehicle Condition", "Road Condition", "Accident Cause",
        "Accident Severity", "Driver Age Group", "Driver Gender", "Region",
    ]
    numeric = [
        "Year", "Visibility Level", "Number of Vehicles Involved", "Speed Limit",
        "Driver Alcohol Level", "Driver Fatigue", "Pedestrians Involved", "Cyclists Involved",
        "Number of Injuries", "Number of Fatalities", "Emergency Response Time",
        "Traffic Volume", "Insurance Claims", "Medical Cost", "Economic Loss", "Population Density",
    ]
    for col in df.columns:
        kind = "categorical" if col in categorical else "numeric"
        notes = ""
        if col == "Visibility Level":
            notes = "e.g. metres"
        elif col == "Driver Alcohol Level":
            notes = "0–1 scale"
        elif col == "Emergency Response Time":
            notes = "e.g. minutes"
        lines.append(f"| {col} | {df[col].dtype} | {kind} | {notes} |\n")

    # Quality
    lines.append("\n### 1.2 Quality checks\n\n")
    missing = df.isnull().sum()
    missing_pct = (missing / len(df) * 100).round(2)
    lines.append("**Missing values:**\n\n")
    lines.append("| Column | Missing | % |\n|--------|---------|---|\n")
    for col in df.columns:
        m, p = missing[col], missing_pct[col]
        if m > 0:
            lines.append(f"| {col} | {m:,} | {p}% |\n")
    if missing.sum() == 0:
        lines.append("No missing values.\n\n")

    dupes = df.duplicated().sum()
    lines.append(f"**Duplicate rows:** {dupes:,}\n\n")

    lines.append("**Key numeric ranges:**\n\n")
    for col in ["Year", "Number of Fatalities", "Number of Injuries", "Speed Limit"]:
        if col in df.columns:
            lo, hi = df[col].min(), df[col].max()
            lines.append(f"- {col}: min={lo}, max={hi}\n")

    # Univariate — categorical
    lines.append("\n### 1.3 Univariate summaries (categorical)\n\n")
    for col in categorical:
        if col not in df.columns:
            continue
        vc = df[col].value_counts()
        lines.append(f"**{col}** ({vc.shape[0]} distinct): ")
        lines.append(", ".join(f"{k}({v:,})" for k, v in vc.head(8).items()))
        if len(vc) > 8:
            lines.append(" ...")
        lines.append("\n")

    # Univariate — numeric
    lines.append("### 1.4 Univariate summaries (numeric)\n\n")
    num_df = df[numeric].describe().round(2)
    lines.append("```\n" + num_df.to_string() + "\n```\n\n")

    # Cross-checks
    lines.append("### 1.5 Cross-checks\n\n")
    country_region = df.groupby("Country")["Region"].nunique()
    mixed = country_region[country_region > 1]
    if len(mixed):
        lines.append(f"**Country vs Region:** Some countries appear in multiple regions (e.g. {list(mixed.index[:5])}).\n\n")
    else:
        lines.append("**Country vs Region:** Each country maps to a single region.\n\n")
    severe_with_fatal = df[(df["Accident Severity"] == "Severe") & (df["Number of Fatalities"] > 0)]
    lines.append(f"**Severe accidents with fatalities:** {len(severe_with_fatal):,} of {len(df[df['Accident Severity']=='Severe']):,} severe.\n\n")

    return "".join(lines)


def section2_geographic(df: pd.DataFrame) -> str:
    """Phase 2: country/region analysis and write CSVs/plots."""
    lines = ["## 2. Geographic findings\n\n"]

    by_country = df.groupby("Country").agg(
        accidents=("Country", "count"),
        total_fatalities=("Number of Fatalities", "sum"),
        total_injuries=("Number of Injuries", "sum"),
    ).reset_index()
    by_country["fatalities_per_accident"] = (by_country["total_fatalities"] / by_country["accidents"]).round(4)
    by_country = by_country.sort_values("accidents", ascending=False)
    by_country.to_csv(BASE / "country_accident_summary.csv", index=False)

    by_region = df.groupby("Region").agg(
        accidents=("Region", "count"),
        total_fatalities=("Number of Fatalities", "sum"),
        total_injuries=("Number of Injuries", "sum"),
    ).reset_index()
    by_region["fatalities_per_accident"] = (by_region["total_fatalities"] / by_region["accidents"]).round(4)
    by_region = by_region.sort_values("accidents", ascending=False)
    by_region.to_csv(BASE / "region_accident_summary.csv", index=False)

    lines.append("**Top countries by accident count:**\n\n```\n")
    lines.append(by_country.head(10).to_string(index=False) + "\n```\n\n**Top regions by accident count:**\n\n```\n")
    lines.append(by_region.head(10).to_string(index=False) + "\n```\n\n")
    lines.append("\n\n")

    # Plots
    fig, axes = plt.subplots(2, 1, figsize=(10, 8))
    by_country.head(12).plot(x="Country", y="accidents", kind="bar", ax=axes[0], legend=False)
    axes[0].set_title("Accidents by country (top 12)")
    axes[0].set_ylabel("Accidents")
    axes[0].tick_params(axis="x", rotation=45)

    by_country.head(12).plot(x="Country", y="total_fatalities", kind="bar", ax=axes[1], legend=False, color="C1")
    axes[1].set_title("Fatalities by country (top 12)")
    axes[1].set_ylabel("Fatalities")
    axes[1].tick_params(axis="x", rotation=45)
    plt.tight_layout()
    plt.savefig(BASE / "geo_country_accidents_fatalities.svg", format="svg")
    plt.close()

    fig, ax = plt.subplots(figsize=(8, 5))
    by_region.plot(x="Region", y="accidents", kind="bar", ax=ax, legend=False)
    ax.set_title("Accidents by region")
    ax.set_ylabel("Accidents")
    ax.tick_params(axis="x", rotation=45)
    plt.tight_layout()
    plt.savefig(BASE / "geo_region_accidents.svg", format="svg")
    plt.close()

    lines.append("Plots saved: `geo_country_accidents_fatalities.svg`, `geo_region_accidents.svg`.\n\n")
    return "".join(lines)


def main():
    df = load_data()
    part1 = section1_data_structure(df)
    part2 = section2_geographic(df)
    with open(SUMMARY_PATH, "w") as f:
        f.write(part1)
        f.write(part2)
    print(f"Wrote {SUMMARY_PATH} (sections 1–2). CSVs and SVGs in {BASE}.")


if __name__ == "__main__":
    main()
