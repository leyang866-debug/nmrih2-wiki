/**
 * Site configuration — the single source of truth for game-specific metadata.
 */

export interface SiteConfig {
  name: string;
  shortName: string;
  description: string;
  domain: string;
  tagline: string;
  legalNotice: string;
  social: {
    official: string;
    discord?: string;
    youtube?: string;
    twitter?: string;
    reddit?: string;
  };
  game: {
    name: string;
    platform: string;
    developer: string;
    publisher: string;
    genre: string;
    releaseDate?: string;
  };
  ogImageWidth: number;
  ogImageHeight: number;
  defaultAuthor?: string;
}

export const site: SiteConfig = {
  name: 'No More Room in Hell 2 Wiki',
  shortName: 'NMRIH2',
  description:
    'No More Room in Hell 2 guide — weapons, perks, maps, survival mode, infection, solo training, crossplay and 1.0 updates.',
  domain: 'nomoreroominhell.online',
  tagline: 'Survive, extract, and learn every run.',
  legalNotice:
    'No More Room in Hell 2 Wiki is a fan-made community resource and is not affiliated with or endorsed by Torn Banner Studios.',
  social: {
    official: 'https://www.nmrih2.com/',
    discord: 'https://discord.com/servers/no-more-room-in-hell-211900829307895819',
    youtube: 'https://www.youtube.com/channel/UCygSSHjXjhLdPeDf1SDXqHw',
    twitter: 'https://x.com/nmrih',
    reddit: 'https://www.reddit.com/r/nmrih/',
  },
  game: {
    name: 'No More Room in Hell 2',
    platform: 'PC/PS5/Xbox Series X|S',
    developer: 'Torn Banner Studios',
    publisher: 'Torn Banner Studios',
    genre: 'Co-op Survival Horror FPS',
    releaseDate: '2026-08-11',
  },
  ogImageWidth: 2560,
  ogImageHeight: 1440,
  defaultAuthor: 'NMRIH2 Wiki',
};

/** Absolute site URL (no trailing slash). Falls back to the Astro `site` config. */
export const siteUrl: string = (process.env.SITE_URL || 'https://nomoreroominhell.online').replace(
  /\/$/,
  '',
);

/** Set by the deployment tool when it creates this site's Google services. */
export const ga4MeasurementId = '';
export const googleSiteVerification = '';
