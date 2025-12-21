import os
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.list import TwoLineListItem, MDList
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog  # Import MDDialog here
from kivy.core.window import Window

class ToDoListApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        self.task_list = []
        self.selected_item = None  # Track selected item

        # Set window size (adjust as needed)
        Window.size = (320, 480)

        # Main screen
        screen = MDScreen()

        # Top bar (using custom image)
        top_label = MDLabel(
            text="All TASK",
            font_style="H4",
            halign="center",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),  # White text color
            pos_hint={"center_x": 0.5, "top": 1},
            size_hint_y=None,
            height=50,
        )
        top_label.bind(size=top_label.setter('text_size'))
        screen.add_widget(top_label)

        # Main content (MDList)
        self.task_list_view = MDList()

        # Load tasks from file
        self.openTaskFile()

        for task in self.task_list:
            self.add_task_item(task)

        screen.add_widget(self.task_list_view)

        # Bottom bar (add task button)
        add_button = MDRaisedButton(
            text="ADD TASK",
            pos_hint={"center_x": 0.5, "center_y": 0.1},
            on_release=self.add_task_dialog,
        )
        screen.add_widget(add_button)

        # Delete button (using MDIconButton and custom image)
        delete_icon = MDIconButton(
            icon="delete",  # Assuming "delete.png" is in your project folder
            pos_hint={"center_x": 0.9, "center_y": 0.1},
            on_release=self.deleteTask,
        )
        screen.add_widget(delete_icon)

        return screen

    def add_task_dialog(self, *args):
        self.dialog = MDDialog(
            title="Add Task",
            type="custom",
            content_cls=MDTextField(),
            buttons=[
                MDRaisedButton(
                    text="ADD",
                    on_release=self.add_task
                ),
                MDRaisedButton(
                    text="CANCEL",
                    on_release=self.dismiss_dialog
                ),
            ],
        )
        self.dialog.open()

    def dismiss_dialog(self, *args):
        self.dialog.dismiss()

    def add_task(self, *args):
        new_task = self.dialog.content_cls.text
        if new_task:
            self.task_list.append(new_task)
            self.add_task_item(new_task)
            self.save_tasks_to_file()
            self.dismiss_dialog()

    def add_task_item(self, task):
        item = TwoLineListItem(
            text=task,
            secondary_text="Details about the task",
            on_release=self.select_task,
        )
        self.task_list_view.add_widget(item)

    def select_task(self, instance):
        if self.selected_item:
            self.selected_item.bg_color = (1, 1, 1, 1)  # Deselect previously selected item
        instance.bg_color = (0.5, 0.5, 0.5, 1)  # Select the clicked item
        self.selected_item = instance

    def deleteTask(self, *args):
        if self.selected_item:
            task = self.selected_item.text
            self.task_list.remove(task)
            self.task_list_view.remove_widget(self.selected_item)
            self.selected_item = None  # Reset selected item
            self.save_tasks_to_file()

    def openTaskFile(self):
        try:
            with open("tasklist.txt", "r") as taskfile:
                tasks = taskfile.readlines()

            self.task_list = [task.strip() for task in tasks if task.strip()]

        except FileNotFoundError:
            open('tasklist.txt', 'w')

    def save_tasks_to_file(self):
        with open("tasklist.txt", 'w') as taskfile:
            for task in self.task_list:
                taskfile.write(f"{task}\n")


if __name__ == "__main__":
    ToDoListApp().run()
