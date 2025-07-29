import PyQt6.QtWidgets as qtw
from PyQt6.QtCore import Qt
import pandas as pd

from styles import DARK_MAIN_WINDOW_STYLE
from custom_widgets import LogBox, ActionButton

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Data Preprocessor")
        self.resize(1200, 650)
        self.setStyleSheet(DARK_MAIN_WINDOW_STYLE)

        self.df = None  # Store loaded DataFrame

        # Main layout
        main_layout = qtw.QVBoxLayout(self)
        main_layout.setContentsMargins(16, 16, 16, 16)
        main_layout.setSpacing(12)

        # Heading
        heading = qtw.QLabel("Welcome to Data Preprocessor GUI!")
        heading.setObjectName("Heading")
        heading.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(heading)

        # Horizontal layout for sidebar and main area
        content_layout = qtw.QHBoxLayout()
        main_layout.addLayout(content_layout)

        # Sidebar (vertical layout)
        sidebar = qtw.QVBoxLayout()
        sidebar.setSpacing(16)
        content_layout.addLayout(sidebar, 1)

        # Import and Preview buttons (vertical)
        import_btn = ActionButton("Import Dataset\n(csv or excel)")
        import_btn.clicked.connect(self.load_dataset)
        sidebar.addWidget(import_btn)

        preview_btn = ActionButton("Preview Dataset")
        preview_btn.clicked.connect(self.preview_dataset)
        sidebar.addWidget(preview_btn)

        # 2x2 grid for 4 buttons
        button_grid = qtw.QGridLayout()
        button_grid.setSpacing(10)

        btn1 = ActionButton("Category Encoding")
        btn2 = ActionButton("Data Description")
        btn3 = ActionButton("Feature Scaling")
        btn4 = ActionButton("Data Imputaion")

        button_grid.addWidget(btn1, 0, 0)  # Row 0, Col 0
        button_grid.addWidget(btn2, 0, 1)  # Row 0, Col 1
        button_grid.addWidget(btn3, 1, 0)  # Row 1, Col 0
        button_grid.addWidget(btn4, 1, 1)  # Row 1, Col 1

        sidebar.addLayout(button_grid)

        # Add stretch to push everything to the top
        sidebar.addStretch()


        # Main area (table and logs)
        main_area = qtw.QVBoxLayout()
        content_layout.addLayout(main_area, 4)

        # Dataset Preview Label
        preview_label = qtw.QLabel("Dataset Preview:")
        preview_label.setObjectName("Section")
        main_area.addWidget(preview_label)

        # Table (hidden by default)
        self.table = qtw.QTableWidget()
        self.table.setMinimumHeight(320)
        self.table.hide()
        main_area.addWidget(self.table)

        # Logs label
        logs_label = qtw.QLabel("Logs:")
        logs_label.setObjectName("Section")
        main_area.addWidget(logs_label)

        # Logs box
        self.log_box = LogBox()
        main_area.addWidget(self.log_box)

        # Create a QWidget to hold the button row
        button_row_widget = qtw.QWidget()
        button_row_layout = qtw.QHBoxLayout(button_row_widget)
        button_row_layout.setContentsMargins(0, 0, 0, 0)
        button_row_layout.addStretch()  # Pushes buttons to the right

        help_btn = ActionButton("Help")
        help_btn.clicked.connect(self.show_help)
        export_btn = ActionButton("Export Dataset (csv)")
        export_btn.clicked.connect(self.export_dataset)

        button_row_layout.addWidget(help_btn)
        button_row_layout.addWidget(export_btn)

        # Add the QWidget (not the layout) to your main_area layout
        main_area.addWidget(button_row_widget)


    # Function to show help message
    def show_help(self):
        help_text = (
            "Welcome to the Data Preprocessor GUI!\n\n"
            "1. Import Dataset: Load a CSV or Excel file to preview its contents.\n"
            "2. Preview Dataset: View the loaded dataset in a table format.\n"
            "3. Export Dataset: Save the current dataset as a CSV file.\n"
            "4. Help: Show this help message."
        )
        qtw.QMessageBox.information(self, "Help", help_text)

        
    # Function to load dataset from file
    def load_dataset(self):
        file_dialog = qtw.QFileDialog(self)
        file_dialog.setNameFilters(["CSV Files (*.csv)", "Excel Files (*.xlsx *.xls)"])
        if file_dialog.exec():
            file_path = file_dialog.selectedFiles()[0]
            try:
                if file_path.endswith(".csv"):
                    self.df = pd.read_csv(file_path)
                else:
                    self.df = pd.read_excel(file_path)
                self.log_box.append(f"Loaded: {file_path}")
            except Exception as e:
                self.log_box.append(f"Error loading file: {e}")


    # Function to preview the loaded dataset
    def preview_dataset(self):
        if self.df is not None:
            self.show_dataframe(self.df)
            self.table.show()
            self.log_box.append("Previewed dataset.")
        else:
            self.log_box.append("No dataset loaded. Please import a dataset first.")


    # Function to display DataFrame in the table widget
    def show_dataframe(self, df):
        self.table.setRowCount(df.shape[0])
        self.table.setColumnCount(df.shape[1])
        self.table.setHorizontalHeaderLabels([str(col) for col in df.columns])
        for row in range(df.shape[0]):
            for col in range(df.shape[1]):
                value = df.iat[row, col]
                item = qtw.QTableWidgetItem("" if pd.isna(value) else str(value))
                self.table.setItem(row, col, item)
        self.table.resizeColumnsToContents()

    # Function to export the dataset to a CSV file
    def export_dataset(self):
        if self.df is None:
            self.log_box.append("No dataset to export.")
            return
        file_dialog = qtw.QFileDialog(self)
        file_dialog.setAcceptMode(qtw.QFileDialog.AcceptMode.AcceptSave)
        file_dialog.setNameFilter("CSV Files (*.csv)")
        if file_dialog.exec():
            file_path = file_dialog.selectedFiles()[0]
            try:
                self.df.to_csv(file_path, index=False)
                self.log_box.append(f"Exported: {file_path}")
            except Exception as e:
                self.log_box.append(f"Error exporting file: {e}")



# Main function to run the application
if __name__ == "__main__":
    app = qtw.QApplication([])
    window = MainWindow()
    window.show()
    app.exec()