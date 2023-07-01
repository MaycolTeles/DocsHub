"""
Module containing the "TkinterUI" Class.
TODO: FIX THIS MODULE
"""

import json
import tkinter as tk

import customtkinter

from .functions import functions
from ...interfaces import UI


customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class TkinterUI(UI, customtkinter.CTk):
    """
    Class to represent a "Tkinter" UserInterface.
    """

    def execute(self) -> None:
        """"""
        self._create_interface()
        self.mainloop()

    def _create_interface(self) -> None:
        """"""
        self._setup()
        self._main_frame_setup()
        self._create_frames()

    def _setup(self) -> None:
        """"""
        self.title("DocsHub")
        self.attributes("-zoomed", True)

        # call .on_closing() when app gets closed
        self.protocol("WM_DELETE_WINDOW", self._on_closing)

    def _create_frames(self) -> None:
        """"""
        self._create_options_frame()
        self._create_documents_frame()

    def _main_frame_setup(self) -> None:
        """"""
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def _create_options_frame(self) -> None:
        """"""
        # configure grid layout (1x11)
        frm_options = customtkinter.CTkFrame(
            master=self,
            corner_radius=20
        )
        frm_options.grid(row=0, column=0, pady=10, padx=10, sticky="ns")

        frm_options.grid_rowconfigure(0, minsize=10)  # empty row with minsize as spacing
        frm_options.grid_rowconfigure(1, minsize=20)  # empty row with minsize as spacing
        frm_options.grid_rowconfigure(2, minsize=20)  # empty row with minsize as spacing
        frm_options.grid_rowconfigure(3, minsize=20)  # empty row with minsize as spacing
        frm_options.grid_rowconfigure(4, minsize=20)  # empty row with minsize as spacing
        frm_options.grid_rowconfigure(5, weight=1)    # empty row as spacing
        frm_options.grid_rowconfigure(6, minsize=10)  # empty row with minsize as spacing
        frm_options.grid_rowconfigure(7, minsize=20)  # empty row with minsize as spacing

        lbl_options = customtkinter.CTkLabel(
            master=frm_options,
            text="OPTIONS",
            font=("Roboto Medium", 24) # font name and size in px
        )
        lbl_options.grid(row=0, column=0, pady=10, padx=10)

        lbl_space = customtkinter.CTkLabel(master=frm_options, text="")
        lbl_space.grid(row=5, column=0)

        lbl_mode = customtkinter.CTkLabel(master=frm_options, text="Appearance Mode:")
        lbl_mode.grid(row=6, column=0, pady=0, padx=20)

        mnu_appearance = customtkinter.CTkOptionMenu(
            master=frm_options,
            values=["Dark", "Light", "System"],
            command=self._change_appearance_mode
        )
        mnu_appearance.grid(row=7, column=0, pady=(0,20), padx=20)

    def _create_documents_frame(self) -> None:
        """
        Private Method to create the Charts Frame
        """
        self._frm_charts = customtkinter.CTkFrame(
            master=self,
            corner_radius=20
        )
        self._frm_charts.grid(row=0, column=1, pady=10, padx=10, sticky="nswe")

        lbl_frame_title = customtkinter.CTkLabel(
            master=self._frm_charts,
            text="DOCUMENTS",
            font=("Roboto Medium", 24) # font name and size in px
        )
        lbl_frame_title.grid(column=0, row=0, padx=10, pady=10)

        self._frm_charts.grid_columnconfigure(0, weight=1)

        lbl_comprovante_residencia = customtkinter.CTkLabel(
            master=self._frm_charts,
            text="Comprovante Residencia",
            font=("Roboto Medium", 24) # font name and size in px
        )
        lbl_comprovante_residencia.grid(column=0, row=1, padx=10, pady=10)

        lbl_cpf = customtkinter.CTkLabel(
            master=self._frm_charts,
            text="CPF",
            font=("Roboto Medium", 24) # font name and size in px
        )
        lbl_cpf.grid(column=0, row=2, padx=10, pady=10)

        lbl_rg = customtkinter.CTkLabel(
            master=self._frm_charts,
            text="RG",
            font=("Roboto Medium", 24) # font name and size in px
        )
        lbl_rg.grid(column=0, row=3, padx=10, pady=10)

    def _change_appearance_mode(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def _on_closing(self):
        """"""
        self.destroy()
