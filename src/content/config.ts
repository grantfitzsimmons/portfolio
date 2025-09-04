import { defineCollection, z } from 'astro:content'

function removeDupsAndLowerCase(array: string[]) {
	if (!array.length) return array
	const lowercaseItems = array.map((str) => str.toLowerCase())
	const distinctItems = new Set(lowercaseItems)
	return Array.from(distinctItems)
}

const post = defineCollection({
	type: 'content',
	schema: ({ image }) =>
		z.object({
			title: z.string().max(60),
			description: z.string().min(50).max(160),
			publishDate: z
				.union([z.string().regex(/^\d{4}-\d{2}-\d{2}$/), z.date()])
				.transform((val) => (val instanceof Date ? val : new Date(val))),
			updatedDate: z
				.union([z.string().regex(/^\d{4}-\d{2}-\d{2}$/), z.date()])
				.optional()
				.transform((val) => (val ? (val instanceof Date ? val : new Date(val)) : undefined)),
			coverImage: z
				.object({
					// Allow either a local content asset (optimized via astro:assets)
					// or a public path string like "/images/cover.jpg"
					src: z.union([image(), z.string().regex(/^\//)]),
					alt: z.string()
				})
				.optional(),
			draft: z.boolean().default(false),
			tags: z.array(z.string()).default([]).transform(removeDupsAndLowerCase),
			ogImage: z.string().optional()
		})
})

export const collections = { post }
