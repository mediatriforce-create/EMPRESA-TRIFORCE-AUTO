import type { Metadata } from "next";
import { Playfair_Display, Inter } from "next/font/google";
import "./globals.css";

const playfair = Playfair_Display({
  subsets: ["latin"],
  weight: ["700"],
  variable: "--font-playfair",
  display: "swap",
});

const inter = Inter({
  subsets: ["latin"],
  weight: ["400", "500", "700"],
  variable: "--font-inter",
  display: "swap",
});

export const metadata: Metadata = {
  title: "Dr. Rafael Fonseca | Harmonizacao Facial e Corporal em Marica/RJ",
  description:
    "Dr. Rafael Fonseca e especialista em harmonizacao facial, corporal e intima masculina. Atende em Marica e Niteroi (Icarai). Avaliacao gratuita. Resultado natural, sem exagero.",
  keywords: [
    "harmonizacao facial Marica",
    "harmonizacao corporal Marica",
    "botox Marica",
    "preenchimento labial Marica",
    "harmonizacao intima masculina Marica",
    "medico estetico Marica",
    "Dr Rafael Fonseca",
    "harmonizacao Niteroi",
    "bioestimulador de colageno Marica",
  ],
  authors: [{ name: "Dr. Rafael Fonseca" }],
  robots: "index, follow",
  openGraph: {
    title: "Dr. Rafael Fonseca | Harmonizacao Facial e Corporal em Marica/RJ",
    description:
      "Especialista em harmonizacao facial, corporal e intima masculina em Marica e Niteroi. Resultado natural. Avaliacao gratuita.",
    type: "website",
    locale: "pt_BR",
  },
};

const schemaOrg = {
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": ["LocalBusiness", "MedicalBusiness", "Physician"],
      "@id": "https://drrafaelfonseca.com.br/#business",
      name: "Dr. Rafael Fonseca - Harmonizacao Facial e Corporal",
      description:
        "Especialista em harmonizacao facial, corporal e intima masculina em Marica e Niteroi. Resultado natural sem exagero.",
      url: "https://drrafaelfonseca.com.br",
      telephone: "+5521966832487",
      priceRange: "$$",
      image: "https://drrafaelfonseca.com.br/images/post_06.jpg",
      address: [
        {
          "@type": "PostalAddress",
          addressLocality: "Marica",
          addressRegion: "RJ",
          addressCountry: "BR",
        },
        {
          "@type": "PostalAddress",
          addressLocality: "Niteroi",
          addressRegion: "RJ",
          streetAddress: "Icarai",
          addressCountry: "BR",
        },
      ],
      geo: {
        "@type": "GeoCoordinates",
        latitude: -22.9189,
        longitude: -42.8183,
      },
      openingHoursSpecification: [
        {
          "@type": "OpeningHoursSpecification",
          dayOfWeek: [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
          ],
        },
      ],
      hasOfferCatalog: {
        "@type": "OfferCatalog",
        name: "Procedimentos de Harmonizacao",
        itemListElement: [
          {
            "@type": "Offer",
            itemOffered: {
              "@type": "MedicalProcedure",
              name: "Harmonizacao Facial",
            },
          },
          {
            "@type": "Offer",
            itemOffered: {
              "@type": "MedicalProcedure",
              name: "Harmonizacao Corporal",
            },
          },
          {
            "@type": "Offer",
            itemOffered: {
              "@type": "MedicalProcedure",
              name: "Harmonizacao Intima Masculina",
            },
          },
        ],
      },
      sameAs: ["https://www.instagram.com/drrafaelfonsecamedico/"],
    },
  ],
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="pt-BR" className={`${playfair.variable} ${inter.variable}`}>
      <head>
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(schemaOrg) }}
        />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" sizes="any" />
      </head>
      <body className="antialiased">{children}</body>
    </html>
  );
}
