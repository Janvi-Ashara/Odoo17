/** @odoo-module **/

import { loadJS } from "@web/core/assets";
import { Component, onWillStart, onMounted, onWillUpdateProps, useRef } from "@odoo/owl";

export class ChartRenderer extends Component {
    setup() {
        this.chartRef = useRef("chart");
        this.chart = null;

        // Load Chart.js before rendering
        onWillStart(async () => {
            await loadJS("https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.5.0/chart.umd.min.js");
        });

        // First render
        onMounted(() => this.renderChart(this.props));

        // Re-render whenever props change
        onWillUpdateProps((nextProps) => {
            this.renderChart(nextProps);
        });
    }

    renderChart(props) {
        const labels = props.labels || [];
        const values = props.values || [];
        const percentages = props.percentages || [];

        if (!this.chartRef.el) {
            console.warn("Canvas not ready");
            return;
        }

        const ctx = this.chartRef.el.getContext("2d");
        if (!ctx) {
            console.warn("No context found on canvas");
            return;
        }

        // Destroy previous chart before re-render
        if (this.chart) {
            this.chart.destroy();
        }

        this.chart = new Chart(ctx, {
            type: props.type || "bar",
            data: {
                labels: labels,
                datasets: [
                    {
                        label: props.title || "Top Products",
                        data: values,
                        backgroundColor: [
                            "#36A2EB",
                            "#FF6384",
                            "#FFCE56",
                            "#4BC0C0",
                            "#9966FF",
                        ],
                    },
                ],
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                animation: false,
                plugins: {
                    legend: { position: "bottom" },
                    title: {
                        display: true,
                        text: props.title || "",
                    },
                    tooltip: {
                        callbacks: {
                            //  Show values + percentage
                            label: (context) => {
                                const value = context.raw;
                                const pct = percentages?.[context.dataIndex] ?? 0;
                                return `${value} units (${pct >= 0 ? "+" : ""}${pct}%)`;
                            },
                        },
                    },
                },
            },
        });
    }
}

ChartRenderer.template = "owl.ChartRenderer";
