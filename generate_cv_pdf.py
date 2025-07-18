from fpdf import FPDF
from PIL import Image

ACCENT = (255, 77, 90)
BG_SIDEBAR = (245, 245, 245)

class CVPDF(FPDF):
    def header(self):
        pass
    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 10)
        self.set_text_color(150, 150, 150)
        self.cell(0, 12, f'Page {self.page_no()}', 0, 0, 'C')

pdf = CVPDF(format='A4')
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=10)

# Dimensions
page_w = pdf.w - 2 * pdf.l_margin
page_h = pdf.h - pdf.t_margin - pdf.b_margin
col_gap = 14
col_w = (page_w - col_gap) // 2
left_x = pdf.l_margin
right_x = pdf.l_margin + col_w + col_gap

# --- HEADER WITH PHOTO AND INFO SIDE BY SIDE ---
header_top = pdf.t_margin + 8
img_size = 26
img_x = pdf.l_margin + 6
img_y = header_top
pdf.image('pireire.jpeg', x=img_x, y=img_y, w=img_size, h=img_size)

header_text_x = img_x + img_size + 8
header_text_w = page_w - (header_text_x - pdf.l_margin)
header_text_y = img_y

pdf.set_xy(header_text_x, header_text_y)
pdf.set_font('helvetica', 'B', 14)
pdf.set_text_color(*ACCENT)
pdf.cell(header_text_w, 7, 'Irenej Bozovicar', ln=1, align='L')

pdf.set_font('helvetica', '', 10)
pdf.set_text_color(30, 30, 30)
pdf.set_x(header_text_x)
pdf.cell(header_text_w, 5, 'Sales Engineering & Integration Support Manager', ln=1, align='L')

pdf.set_font('helvetica', '', 9)
pdf.set_text_color(100, 100, 100)
pdf.set_x(header_text_x)
pdf.cell(header_text_w, 4, 'Ljubljana, Slovenia', ln=1, align='L')

pdf.set_font('helvetica', 'I', 9)
pdf.set_text_color(*ACCENT)
pdf.set_x(header_text_x)
pdf.cell(header_text_w, 5, 'Architecting the bridge between technology and business', ln=1, align='L')

header_end_y = max(img_y + img_size, pdf.get_y()) + 6

# --- COLUMNS START BELOW HEADER ---
col_top = header_end_y

# --- LEFT COLUMN ---
left_y = col_top
pdf.set_fill_color(*BG_SIDEBAR)
pdf.rect(left_x, left_y, col_w, page_h - (col_top - pdf.t_margin), 'F')

# Contact Info
pdf.set_xy(left_x, left_y)
pdf.set_font('helvetica', 'B', 10)
pdf.set_text_color(*ACCENT)
pdf.cell(col_w, 7, 'Contact', ln=1, align='L')
pdf.set_font('helvetica', '', 9)
contact_links = [
    ('bozoire@gmail.com', 'mailto:bozoire@gmail.com'),
    ('linkedin.com/in/irenej-bozovicar-764a75123', 'https://linkedin.com/in/irenej-bozovicar-764a75123'),
    ('github.com/PireIre', 'https://github.com/PireIre'),
]
for label, url in contact_links:
    pdf.set_x(left_x)
    pdf.set_text_color(0, 102, 204)  # blue for links
    pdf.cell(col_w, 5, label, ln=1, align='L', link=url)
    left_y = pdf.get_y()
pdf.set_text_color(50, 50, 50)  # reset to normal for rest of section
left_y += 3

# Skills
pdf.set_xy(left_x, left_y)
pdf.set_font('helvetica', 'B', 10)
pdf.set_text_color(*ACCENT)
pdf.cell(col_w, 7, 'Skills', ln=1, align='L')
pdf.set_font('helvetica', '', 9)
pdf.set_text_color(50, 50, 50)
skills = [
    'Sales Engineer', 'Team Management', 'Technical Support',
    'JavaScript', 'Tech Docs', 'API Integration', 'Python', 'AI Integration', 'React', 'Salesforce'
]
for s in skills:
    pdf.set_x(left_x + 6)
    pdf.cell(col_w - 12, 5, f'- {s}', ln=1)
    left_y = pdf.get_y()
left_y += 3

# Projects (left column)
pdf.set_xy(left_x, left_y)
pdf.set_font('helvetica', 'B', 10)
pdf.set_text_color(*ACCENT)
pdf.cell(col_w, 7, 'Projects', ln=1, align='L')
pdf.set_font('helvetica', '', 9)
pdf.set_text_color(30, 30, 30)
projects = [
    ('Integration Demo Tool', 'Google Chrome extension for debugging and demoing projects on customer websites. Internal demo app for sales to customize demos.'),
    ('Technical Documentation Revamp', 'Revamped Bambuser documentation - clarity, usability, infrastructure. Live: bambuser.com/docs/'),
    ('GitHub Profile', 'Personal coding projects: github.com/PireIre'),
]
for title, desc in projects:
    pdf.set_x(left_x + 4)
    pdf.set_font('helvetica', 'B', 9)
    pdf.cell(col_w - 8, 5, title, ln=1)
    left_y = pdf.get_y()
    pdf.set_font('helvetica', '', 9)
    pdf.set_x(left_x + 8)
    pdf.multi_cell(col_w - 12, 5, desc)
    left_y = pdf.get_y() + 2

# Languages (left column)
pdf.set_xy(left_x, left_y)
pdf.set_font('helvetica', 'B', 10)
pdf.set_text_color(*ACCENT)
pdf.cell(col_w, 7, 'Languages', ln=1, align='L')
pdf.set_font('helvetica', '', 9)
pdf.set_text_color(30, 30, 30)
languages = [
    ('English', 'Fluent'),
    ('Slovenian', 'Fluent'),
    ('Swedish', 'Conversational'),
]
for lang, level in languages:
    pdf.set_x(left_x + 6)
    pdf.cell(col_w - 12, 5, f'{lang} ({level})', ln=1)
    left_y = pdf.get_y()

# --- RIGHT COLUMN ---
right_y = col_top

def section_title(pdf, x, y, w, title):
    pdf.set_xy(x, y)
    pdf.set_font('helvetica', 'B', 12)
    pdf.set_text_color(*ACCENT)
    pdf.cell(w, 8, title, ln=1)
    return pdf.get_y()

# Experience
right_y = section_title(pdf, right_x, right_y, col_w, 'Experience')
pdf.set_font('helvetica', '', 9)
pdf.set_text_color(30, 30, 30)
exp = [
    ('Sales Engineering & Integration Support Manager, Bambuser', 'Feb 2024 - Present', [
        'Lead and manage two teams',
        'Lead AI chatbot project',
        'Product testing',
        'Ticketing system transition',
        'Cross-team collaboration',
    ]),
    ('Senior Sales Engineer, Bambuser', 'Jan 2023 - Present', [
        'Technical POC for top enterprise clients (Zara, LVMH, Currys, Elkjop, Adidas, Clarins, others under NDA)',
        'Demo website, technical documentation revamp',
        'Internal tools, integration tutorial videos',
    ]),
    ('Solutions Manager, Bambuser', 'Mar 2022 - Jan 2023', [
        'Managed client implementations',
        'Technical consulting',
        'Internal tools',
    ]),
    ('Integration Support Specialist, Bambuser', 'Jun 2020 - Mar 2022', [
        'Support tickets',
        'Technical meetings',
        'Onboarding',
        'Documentation',
    ]),
]
for title, dates, bullets in exp:
    pdf.set_xy(right_x, right_y)
    pdf.set_font('helvetica', 'B', 9)
    pdf.set_text_color(30, 30, 30)
    pdf.multi_cell(col_w, 5, f'{title} ({dates})')
    right_y = pdf.get_y()
    pdf.set_font('helvetica', '', 9)
    for b in bullets:
        pdf.set_xy(right_x + 6, right_y)
        pdf.multi_cell(col_w - 12, 4, f'- {b}')
        right_y = pdf.get_y()
    right_y += 2

# Education (move to right column)
right_y = section_title(pdf, right_x, right_y, col_w, 'Education')
pdf.set_font('helvetica', '', 9)
pdf.set_text_color(30, 30, 30)
edu = [
    ('KTH Royal Institute of Technology', '2020', 'Software Development Academy (Java)'),
    ('Manhattan University', '2015-2018', 'BSc Pre-Physical Therapy Studies'),
    ('Gimnazija Jesenice', '2011-2014', 'General Studies'),
]
for school, years, detail in edu:
    pdf.set_x(right_x + 4)
    pdf.set_font('helvetica', 'B', 9)
    pdf.cell(col_w - 8, 5, f'{school} ({years})', ln=1)
    right_y = pdf.get_y()
    pdf.set_font('helvetica', '', 9)
    pdf.set_x(right_x + 8)
    pdf.cell(col_w - 12, 4, detail, ln=1)
    right_y = pdf.get_y() + 1

pdf.output('Irenej_Bozovicar_CV.pdf') 