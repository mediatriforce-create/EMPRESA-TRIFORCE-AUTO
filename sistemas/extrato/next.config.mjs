/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    remotePatterns: [],
  },
  experimental: { serverComponentsExternalPackages: ["pdf-parse"] },
};

export default nextConfig;
