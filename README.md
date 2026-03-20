Bava Erukka Bayamae 🗿
A High-Performance, Ad-Free YouTube Client for Android

🚀 Overview

Bava Erukka Bayamae (Why Fear When Bava is Here?) is a lightweight, open-source YouTube clone built specifically for low-resource Android devices. 
Unlike the official application, this project focuses on speed, privacy, and background functionality without the overhead of heavy tracking or forced advertisements.

⚠️ The Problem Statement

Modern video streaming applications have become increasingly resource-intensive, often leading to:
Excessive Ad-Interrupts: Disrupting the learning and entertainment experience.
High RAM Consumption: Making it difficult for older Android devices to maintain a smooth UI.
Background Restrictions: Forcing users into premium subscriptions just to listen to audio while multitasking.
Privacy Concerns: Constant data syncing and tracking in the background.

✅ The Solution

This project provides a "Vampire-themed" (Dark Mode by default) interface that bypasses traditional bottlenecks by utilizing raw stream extraction.
It allows users on older hardware—like the Oppo A5—to enjoy high-quality video playback with minimal battery drain and zero ads.

🛠 Tech StackComponent
Language              Python 3.11
Frontend              Kivy & KivyMD (Cross-platform UI)
Extraction Engine     yt-dlp (Advanced stream metadata extraction)
Video Playback        ffpyplayer (FFmpeg-based high-efficiency player)
Build Toolchain       Buildozer, Android NDK r23b (Custom Spoofed), SDK 34Networkingrequests, urllib3, certifi

✨ Key FeaturesZero-Ad Experience: 

Native ad-blocking by accessing direct video streams.
Background Play: Keep the audio running even when the screen is off or the app is minimized.
Lightweight Architecture: Optimized for devices with limited processing power.
Custom Theming: Integrated with a custom "Nightmare Before Christmas" aesthetic for a unique user experience.
Direct-to-Stream: Bypasses heavy API calls to provide faster loading times.

🏗 Technical Challenges Overcome (The "Bava" Touch)

Building this project wasn't just about writing code; it was about fighting the Android build ecosystem. 
Key technical milestones include:NDK Version Spoofing: Successfully manipulated Buildozer to accept NDK r23b in a modern SDK environment to ensure library compatibility.
Legacy-CGI Implementation: Resolved Python 3.13 compatibility issues by integrating legacy-cgi wrappers for older Cython dependencies.
Gradle Optimization: Manually debugged and repaired corrupted build.gradle templates to resolve "unknown property" errors in modern Gradle 8.x environments.

👨‍💻 About the AuthorJ. Nishanth Raj (BAVA)Passionate Developer: 
Focused on AI Agents, Automation, and Robotics.
Founder: Creator of the Vallaipallam programming language.
Mindset: I love building "crazy stuff" that solves real-world problems through automation. 

Whether it's a robot to fetch parottas or an AI to manage your YouTube, I build with the motto: Risk-u edukkuradhu ellam namma kitta rusk-u sapidura madhiri!

📥 Getting StartedClone the repository:

git clone https://github.com/yourusername/bava-erukka-bayamae.git

Install requirements:
pip install -r requirements.txt

Deploy to Android:
buildozer -v android debug
