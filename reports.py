#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

#this file is imported by reports.py in step 4


def generate_report(attachment, title, paragraph):

    report = SimpleDocTemplate(attachment)
    styles = getSampleStyleSheet()
    report_title = Paragraph(title, styles["h2"])
    report_body = Paragraph(paragraph, styles["Normal"])
    report.build([report_title, report_body])

