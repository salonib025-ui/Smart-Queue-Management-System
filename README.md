A real-time Computer Vision and AI-based queue monitoring system built with OpenCV, YOLOv8, and Python. The application processes camera feed input to detect people, estimate dynamic waiting times, evaluate crowd statuses using a moving average window, trigger real-time UI alerts, and log analytical data for trend visualization.

🌟 Key Features
Real-Time People Detection: Leverages YOLOv8 object detection to identify and count individuals in camera frames.

Moving Average Queue Analysis: Smooths frame-by-frame person counts over time to accurately categorize queue density (Short, Moderate, Long).

Dynamic Wait Time Estimation: Calculates estimated customer wait times based on live occupancy and service rates.

Interactive UI Dashboard: Renders a clean real-time status overlay alongside the visual camera feed.

Crowd Alerts: Displays visual alert banners when crowd density exceeds configured thresholds.

Automated Data Logging: Exports real-time queue metrics and timestamps to CSV files for historical monitoring.

Analytics & Visualizations: Integrated Matplotlib tools to plot historical occupancy trends and peak time metrics.
