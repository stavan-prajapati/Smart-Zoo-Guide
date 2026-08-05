# Smart Zoo Guide – Kamatibaug

## Overview

Smart Zoo Guide – Kamatibaug is an AI-powered web application that identifies animals found at Kamatibaug Zoo (Sayaji Baug), Vadodara, using image processing and deep learning. Users can upload or capture an image of an animal, and the system identifies the species and displays detailed information such as its common name, scientific name, habitat, diet, conservation status, and description.

The project aims to provide an interactive and educational experience for zoo visitors by replacing the limitations of traditional information boards with an intelligent digital platform.

---

## Problem Statement

Information boards in Kamatibaug Zoo have several limitations:

- Information is available only in English and Gujarati.
- Animals may be relocated while information boards remain unchanged.
- Information is limited and not interactive.
- Visitors often require faster and more convenient access to animal information.

This project addresses these issues through an AI-based animal identification system.

---

## Objectives

- Develop an AI-based animal identification system.
- Allow users to upload or capture animal images.
- Preprocess images using OpenCV.
- Classify animals using the MobileNetV2 deep learning model.
- Retrieve animal information from a SQLite database.
- Provide a responsive and user-friendly web interface.
- Improve the educational experience of zoo visitors.

---

## Features

- Animal identification using AI
- Image upload functionality
- Webcam image capture
- Image preprocessing using OpenCV
- Animal classification using MobileNetV2
- Display of:
  - Common Name
  - Scientific Name
  - Habitat
  - Diet
  - Conservation Status
  - Description
- SQLite database integration
- Responsive web interface

---

## Project Structure

```text
CGIP-project/
│
├── docs/
├── src/
│   ├── gui/
│   ├── processing/
│   └── main.py
├── tests/
├── README.md
├── requirements.txt
├── .gitignore
└── .gitattributes
```

---

## Technology Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| Frontend | HTML, CSS, JavaScript, Bootstrap |
| Backend | Flask |
| Image Processing | OpenCV |
| AI Framework | TensorFlow, Keras |
| Deep Learning Model | MobileNetV2 |
| Database | SQLite |
| IDE | Visual Studio Code |
| Version Control | Git & GitHub |

---

## Workflow

1. User opens the web application.
2. User uploads or captures an animal image.
3. OpenCV preprocesses the image.
4. MobileNetV2 predicts the animal species.
5. Animal information is retrieved from the SQLite database.
6. The application displays the identified animal and its details.

---

## Expected Deliverables

- AI-based web application
- Trained MobileNetV2 model
- SQLite database
- Complete source code
- Project documentation
- Test cases
- User manual
- Presentation
- Demonstration video

---

## Future Enhancements

- Interactive zoo navigation
- Multilingual support
- Mobile application
- AI chatbot integration
- Cloud database integration
- Real-time video-based animal identification

---

## Team Members

| Enrollment No. | Name |
|---------------|------------------|
| 24000514 | Stavan Prajapati |
| 24000626 | Het Patel |
| 24001078 | Yash Rathod |

---

## Course

Computer Graphics and Image Processing (CMP513 + CMP514)

Academic Year: 2026

---

## License

This project is developed for academic purposes as part of the Computer Graphics and Image Processing course.