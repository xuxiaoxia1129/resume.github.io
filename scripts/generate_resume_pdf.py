from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "01_个人简历与证明" / "许晓霞-数据产品经理-简历.pdf"


FONT_NAME = "ResumeHeiti"
FONT_PATH = "/System/Library/Fonts/STHeiti Medium.ttc"
pdfmetrics.registerFont(TTFont(FONT_NAME, FONT_PATH, subfontIndex=0))


def p(text, style):
    return Paragraph(text, style)


def bullet(text, style):
    return Paragraph(f"• {text}", style)


def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFont(FONT_NAME, 8)
    canvas.setFillColor(colors.HexColor("#7a7f8a"))
    canvas.drawRightString(200 * mm, 10 * mm, f"许晓霞｜数据产品经理｜第 {doc.page} 页")
    canvas.restoreState()


styles = getSampleStyleSheet()

base = ParagraphStyle(
    "base",
    parent=styles["Normal"],
    fontName=FONT_NAME,
    fontSize=9.4,
    leading=14.2,
    textColor=colors.HexColor("#242933"),
    wordWrap="CJK",
    alignment=TA_LEFT,
)

small = ParagraphStyle(
    "small",
    parent=base,
    fontSize=8.5,
    leading=12.6,
    textColor=colors.HexColor("#4b5563"),
)

title = ParagraphStyle(
    "title",
    parent=base,
    fontSize=22,
    leading=26,
    textColor=colors.HexColor("#111827"),
    spaceAfter=4,
)

subtitle = ParagraphStyle(
    "subtitle",
    parent=base,
    fontSize=10,
    leading=14,
    textColor=colors.HexColor("#374151"),
)

section = ParagraphStyle(
    "section",
    parent=base,
    fontSize=12.2,
    leading=16,
    textColor=colors.HexColor("#1f4b8f"),
    spaceBefore=8,
    spaceAfter=5,
)

job_title = ParagraphStyle(
    "job_title",
    parent=base,
    fontSize=10.8,
    leading=14.5,
    textColor=colors.HexColor("#111827"),
    spaceBefore=5,
    spaceAfter=2,
)

muted = ParagraphStyle(
    "muted",
    parent=base,
    fontSize=8.4,
    leading=12,
    textColor=colors.HexColor("#6b7280"),
)


story = []

header = Table(
    [
        [
            p("许晓霞", title),
            p(
                "上海｜18226758619｜微信 xxx591587117｜xuxiaoxia1129@gmail.com<br/>"
                "GitHub: github.com/xuxiaoxia1129｜求职方向：数据产品经理 / BI 产品经理 / AI 产品经理",
                subtitle,
            ),
        ]
    ],
    colWidths=[36 * mm, 142 * mm],
)
header.setStyle(
    TableStyle(
        [
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ("LINEBELOW", (0, 0), (-1, -1), 0.8, colors.HexColor("#d7dde8")),
        ]
    )
)
story.append(header)

story.append(p("个人优势", section))
for item in [
    "近 10 年产品与设计经验，6 年以上深度负责房地产大数据产品，覆盖 To C 小程序、To B 决策系统、数据平台和后台管理系统。",
    "熟悉复杂数据产品全流程：业务调研、PRD、原型设计、指标口径、数据结构、开发协同、上线验收、数据复盘和持续迭代。",
    "具备 BI 看板、指标体系、埋点治理、用户标签、客户生命周期、地图可视化、行业数据平台和 AI 协作系统经验。",
    "近期转向金融业务数据产品，围绕策略产品、客户经营、服务质量、渠道转化和客诉风控搭建 BI、埋点和数据分析体系。",
    "独立完成紫微斗数数据化解读系统，将传统文化笔记、知识库、规则结构、AI 问答和线上系统结合，体现学习力与系统化能力。",
]:
    story.append(bullet(item, base))

story.append(p("工作经历", section))

jobs = [
    (
        "利多星证券公司｜数据产品 / BI 与数据治理",
        "2026.03 - 2026.06",
        [
            "围绕金融策略产品、投顾服务、客户生命周期、用户行为、客诉风控和渠道转化场景，负责金融数据产品需求梳理、BI 看板设计、指标口径定义、埋点治理和数据质量协同。",
            "私享家 BI 数据看板：梳理策略收益、客户价值、产品运营、客服/投顾服务、订单退款和经营总览等模块，设计管理层驾驶舱和多角色分析路径。",
            "数据埋点治理：建立多端埋点验收和数据质量分析流程，对 APP、小程序、PC、H5 核心事件进行字段质量、趋势稳定性、ID 映射和 URL 清洗规则检查。",
            "AI 客诉与风控：将公域舆情、评论手机号识别、客户匹配、风险触达、安抚处置和复盘流程拆成可产品化的数据链路。",
            "用户分层与客户经营分析：梳理基础信息、行为、资产价值、风险偏好、产品偏好和忠诚度等标签维度，设计客户生命周期与运营分析框架。",
            "股民保护 BI 看板：围绕公域资源、咨询、签约、维权标的和渠道效果，设计业务流程图、指标口径和经营看板结构。",
        ],
    ),
    (
        "上海澜思信息科技有限公司｜数据产品经理",
        "2019.05 - 2025.08",
        [
            "负责公司核心房地产大数据产品体系，覆盖 C 端小程序、B 端决策系统、经纪人工具、数据平台和后台管理系统，面向购房者、开发商、经纪公司与内部业务团队。",
            "负责产品规划、业务调研、需求拆解、原型设计、PRD 编写、版本管理和上线验收，协同技术、运营、商务、客服、开发商和中介门店持续迭代产品。",
            "一房一万新房小程序：主导 6 年，从 2019 年推翻重做到 2020 年 5.0 上线，后续伴随上海楼市政策持续迭代，小程序累计用户 80 万+。",
            "小房书：面向中小中介门店、夫妻店和个体经纪人的二手房数据产品，经历地图数据展示、权限配置、楼盘数据售卖和门店市占率分析，服务上百家付费门店。",
            "城市地图 / CityMap：面向开发商和经纪公司的 B 端数据决策系统，经历 0-1 梳理、1.0 开发和多年维护迭代，打通土地拍卖、新房成交、竣工、入住、二手房流通等房地产全生命周期数据。",
            "数据中心 / RAS / 基价模型：围绕楼盘基价、板块得分、价格校准和模型解释搭建数据中心能力，让前台产品具备更稳定的数据算法基础。",
            "红盘系统与挂牌查价：覆盖新房认购、定价、户配、销售、舆情、客户画像、二手房挂牌与成交查询等场景，其中挂牌查价阶段性获得 2 万+用户。",
        ],
    ),
    (
        "个人项目与知识系统｜AI 产品 / 知识工程 / 全栈实践",
        "2025.09 - 至今",
        [
            "紫微斗数数据化解读系统：基于两年传统文化学习和上百万字笔记，将紫微斗数解盘流程拆成命盘结构、知识库、规则框架、AI 解读和积分交互系统，并上线为完整网站。",
            "证券考试辅助项目：将证券从业题库、讲义、真题和练习过程结构化，搭建辅助备考工具，体现资料处理、自动化和学习产品化能力。",
            "FlowMindLab / Obsidian 个人知识库：以 Obsidian 仓库作为内容源，通过 Quartz 发布上线，持续沉淀知识管理、个人记录、AI、机器学习、Python、MySQL 和紫微斗数主题。",
        ],
    ),
    (
        "上海展宏网络科技有限公司｜产品设计师",
        "2018.06 - 2019.05",
        [
            "负责 Web、PC、移动端、H5、小程序和 App 的产品原型、交互设计与 UI 设计，参与传统文化、AI 面相识别、手相识别、算命 App/小程序和工具类产品设计落地。",
            "参与产品从 0-1 的需求沟通、竞品分析、交互流程、视觉风格和界面设计，与开发协作推进上线。",
        ],
    ),
    (
        "上海百纬健康科技有限公司｜产品设计",
        "2017.01 - 2018.05",
        [
            "参与医疗健康 App、官网和微信端产品设计，与产品、研发和测试团队协作，推进移动端产品体验优化和品牌视觉建设。",
            "负责手机客户端、官网、H5 和活动页面的 UI 设计与交互优化，制定视觉规范并收集用户反馈。",
        ],
    ),
]

for company, date, bullets in jobs:
    row = Table(
        [[p(f"<b>{company}</b>", job_title), p(date, muted)]],
        colWidths=[130 * mm, 48 * mm],
    )
    row.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("ALIGN", (1, 0), (1, 0), "RIGHT")]))
    story.append(row)
    for item in bullets:
        story.append(bullet(item, small if len(item) > 65 else base))
    story.append(Spacer(1, 2))

story.append(p("专业技能", section))
skills = [
    ["数据产品", "指标体系、数据口径、BI 看板、经营驾驶舱、数据集设计、用户标签、客户生命周期"],
    ["行业数据", "房地产土地/新房/二手房全生命周期数据、金融客户行为与经营分析、业务流程建模"],
    ["产品设计", "需求调研、原型设计、PRD、版本规划、上线验收、用户路径、后台管理系统、B 端工具"],
    ["数据治理", "埋点方案、埋点验收、字段质量、ID 映射、宽表清洗、数据可用性判断"],
    ["AI 与知识系统", "AI 协作编程、知识库结构化、Markdown/Obsidian、Quartz、传统知识规则化"],
    ["工具使用", "Axure、Figma、Sketch、XMind、Excel、SQL 基础、Python 学习与数据处理、Markdown"],
]
skill_table = Table(
    [[p(f"<b>{a}</b>", base), p(b, base)] for a, b in skills],
    colWidths=[30 * mm, 148 * mm],
)
skill_table.setStyle(
    TableStyle(
        [
            ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#e1e6ef")),
            ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#f5f7fb")),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 5),
            ("RIGHTPADDING", (0, 0), (-1, -1), 5),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ]
    )
)
story.append(skill_table)

story.append(p("教育经历", section))
story.append(p("<b>宿州学院｜网络工程｜本科</b>　2012 - 2016", base))
for item in ["2013 年中国机器人大赛二等奖", "2015 年国家励志奖学金", "2016 年优秀毕业生"]:
    story.append(bullet(item, base))

story.append(p("作品集入口", section))
story.append(
    p(
        "项目作品集：本地简历网站已整理紫微斗数数据化解读系统、利多星金融数据产品、澜思房地产大数据产品、证券考试辅助项目、FlowMindLab 知识库等案例。",
        base,
    )
)

doc = BaseDocTemplate(
    str(OUTPUT),
    pagesize=A4,
    leftMargin=16 * mm,
    rightMargin=16 * mm,
    topMargin=14 * mm,
    bottomMargin=16 * mm,
    title="许晓霞-数据产品经理-简历",
    author="许晓霞",
)
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal")
doc.addPageTemplates([PageTemplate(id="resume", frames=[frame], onPage=on_page)])
doc.build(story)
print(OUTPUT)
