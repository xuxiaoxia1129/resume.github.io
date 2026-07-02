export default {
  title: '许晓霞',
  description: '数据产品经理、AI 产品原型构建者、知识管理实践者',
  lang: 'zh-CN',
  cleanUrls: false,
  srcExclude: ['.vitepress/dist/**'],
  themeConfig: {
    nav: [
      { text: '首页', link: '/' },
      { text: '关于我', link: '/about' },
      { text: '项目作品', link: '/projects/' },
      { text: '能力结构', link: '/skills/' },
      { text: '简历', link: '/resume' },
      { text: '联系', link: '/contact' },
      { text: '⬇ PDF 简历', link: '/assets/resume-xuxiaoxia.pdf' }
    ],
    sidebar: {
      '/projects/': [
        {
          text: '项目作品',
          items: [
            { text: '项目总览', link: '/projects/' },
            {
              text: '01. 个人项目',
              collapsed: false,
              items: [
                { text: '紫微斗数数据化解读系统', link: '/projects/personal/ziwei-ai-system' }
              ]
            },
            {
              text: '02. 利多星金融数据产品',
              collapsed: false,
              items: [
                { text: '专题总览', link: '/projects/liduoxing/' },
                { text: '私享家 BI 数据看板', link: '/projects/liduoxing/sixiangjia-bi' },
                { text: '数据埋点治理', link: '/projects/liduoxing/tracking-governance' },
                { text: 'AI 客诉与风控', link: '/projects/liduoxing/ai-complaint-risk' },
                { text: '用户分层与客户经营分析', link: '/projects/liduoxing/user-tags' },
                { text: '股民保护 BI 看板', link: '/projects/liduoxing/woodpecker-bi' }
              ]
            },
            {
              text: '03. 澜思房地产大数据产品',
              collapsed: false,
              items: [
                { text: '专题总览', link: '/projects/lansi/' },
                { text: '一房一万新房小程序', link: '/projects/lansi/yifangyiwan-new-home' },
                { text: '小房书', link: '/projects/lansi/xiaofangshu-res' },
                { text: '城市地图 / CityMap', link: '/projects/lansi/citymap' },
                { text: '数据中心 / RAS / 基价模型', link: '/projects/lansi/data-center-ras' },
                { text: '红盘系统', link: '/projects/lansi/red-house-system' },
                { text: '挂牌查价', link: '/projects/lansi/listing-price-check' }
              ]
            },
            {
              text: '04. 个人工具与知识库',
              collapsed: false,
              items: [
                { text: '专题总览', link: '/projects/knowledge-tools/' },
                { text: '证券考试辅助项目', link: '/projects/knowledge-tools/securities-exam-tool' },
                { text: 'FlowMindLab / Obsidian 个人知识库', link: '/projects/knowledge-tools/flowmindlab-quartz' }
              ]
            }
          ]
        }
      ],
      '/skills/': [
        {
          text: '能力结构',
          items: [
            { text: '能力总览', link: '/skills/' },
            { text: '数据产品', link: '/skills/data-product' },
            { text: 'AI 原型与知识系统', link: '/skills/ai-prototyping' },
            { text: '知识管理与内容系统', link: '/skills/knowledge-system' }
          ]
        }
      ],
      '/': [
        {
          text: '个人作品集',
          items: [
            { text: '首页', link: '/' },
            { text: '关于我', link: '/about' },
            { text: '项目作品', link: '/projects/' },
            { text: '能力结构', link: '/skills/' },
            { text: '简历', link: '/resume' },
            { text: '联系', link: '/contact' }
          ]
        }
      ]
    },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/xuxiaoxia1129' }
    ],
    search: {
      provider: 'local'
    },
    footer: {
      message: '个人简历与项目作品集',
      copyright: 'Copyright © 2026 许晓霞'
    },
    outline: {
      label: '本页目录',
      level: [2, 3]
    },
    docFooter: {
      prev: '上一页',
      next: '下一页'
    },
    darkModeSwitchLabel: '外观',
    sidebarMenuLabel: '目录',
    returnToTopLabel: '返回顶部'
  }
}
