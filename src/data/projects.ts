export interface ProjectCardItem {
	href: string
	heading: string
	subheading: string
	imagePath: string
	altText: string
}

export const projectCards: ProjectCardItem[] = [
	{
		href: '/projects/specify-7/',
		heading: 'Specify 7',
		subheading:
			'A collections management platform for natural history museums and research collections. 100% open-source and free to use.',
		imagePath: '/src/pages/projects/specify-7/screenshots/homepage.png',
		altText: 'Specify 7'
	},
    {
		href: '/projects/specify-software/',
		heading: 'Specify Collections Consortium Website',
		subheading: 'Built from scratch using Astro, JavaScript, and TypeScript. Integrated the new logo and branding across the site while meeting top SEO and accessibility standards.',
		imagePath: '/src/pages/projects/specify-software/screenshots/homepage.png',
		altText: 'Specify Collections Consortium website'
	},
	{
		href: '/projects/ready-rental/',
		heading: 'Ready Rental Website',
		subheading:
			'Built with Squarespace as web builder and architect. Developed pipelines for rental requests, scheduling, and contact forms. Integrated with Google Workspace for email and calendar management.',
		imagePath: '/src/pages/projects/ready-rental/screenshots/homepage.png',
		altText: 'Ready Rental website homepage'
	},
	{
		href: '/projects/geo-specify/',
		heading: 'GeoSpecify',
		subheading:
			'An initiative to expand Specify for earth sciences, supporting geoscience collections of rocks, minerals, and meteorites, is co-led by the Swiss Natural History Museums of Bern, Basel, and Geneva, funded by SwissCollNet.',
		imagePath: '/src/assets/geospecify.png',
		altText: 'GeoSpecify'
	},
	{
		href: '/projects/specify-community-forum/',
		heading: 'Specify Community Forum',
		subheading:
			'Established and maintain the Specify Community Forum, a platform for Specify users to collaborate, discuss, and read documentation.',
		imagePath: '/src/assets/speciforum.png',
		altText: 'Speciforum'
	},
	{
		href: '/projects/system-admin-docs/',
		heading: 'System Administration and Documentation',
		subheading:
			'Standardized global DNS into Cloudflare, hardened edge security (WAF/bot controls), and managed 150+ RDS databases plus 40+ EC2 instances with unified deployment and monitoring practices.',
		imagePath: '/src/assets/techdocs.png',
		altText: 'System admin documentation'
	}
]
