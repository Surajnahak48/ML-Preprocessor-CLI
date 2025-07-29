# HEADING_STYLE = """
#     font-size: 24px;
#     font-weight: bold;
#     margin: 5px;

#     color: #0078d7;
# """

# MAIN_WINDOW_STYLE = """
#     background-color: #f0f0f0;
# """

# styles.py

DARK_MAIN_WINDOW_STYLE = """
    QWidget {
        background-color: #181c24;
        color: #f0f0f0;
        font-family: 'Segoe UI', Arial, sans-serif;
        font-size: 15px;
    }
    QTableWidget {
        background-color: #23283a;
        color: #f0f0f0;
        border-radius: 8px;
    }
    QPushButton {
        background-color: #23283a;
        color: #fff;
        border-radius: 2px;
        padding: 4px 8px;
        font-size: 13px;
        font-weight: 500;
        min-height: 10px;
        min-width: 20px;
    }
    QPushButton:hover {
        background-color: #2d334d;
    }
    QLineEdit, QTextEdit {
        background-color: #23283a;
        color: #f0f0f0;
        border-radius: 6px;
        padding: 6px;
    }
    QLabel#Heading {
        font-size: 32px;
        font-weight: bold;
        color: #4f8cff;
        background: #23283a;
        border-radius: 12px;
        padding: 20px 0 20px 0;
    }
    QLabel#Section {
        font-size: 18px;
        font-weight: 600;
        color: #fff;
        margin-top: 12px;
        margin-bottom: 6px;
    }
"""

# SCROLLBAR_STYLE = """
# QScrollBar:vertical {
#     width: 18px;
#     background: #23283a;
#     margin: 0px 0px 0px 0px;
#     border-radius: 8px;
# }
# QScrollBar::handle:vertical {
#     background: #4f8cff;
#     min-height: 30px;  /* Increase this for a thicker/longer handle */
#     border-radius: 8px;
# }
# QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
#     height: 0px;
# }
# """