export interface NavigationItem {
  key: string;
  path: string;
  icon: string;
  isContentType: true;
  order?: number;
}

export const NAVIGATION_CONFIG: NavigationItem[] = [
  { key: 'weapons', path: '/weapons', icon: 'lucide:crosshair', isContentType: true, order: 1 },
  { key: 'maps', path: '/maps', icon: 'lucide:map', isContentType: true, order: 2 },
  { key: 'perks', path: '/perks', icon: 'lucide:badge-plus', isContentType: true, order: 3 },
  { key: 'survival', path: '/survival-mode', icon: 'lucide:shield', isContentType: true, order: 4 },
  { key: 'tips', path: '/tips', icon: 'lucide:lightbulb', isContentType: true, order: 5 },
  { key: 'update', path: '/1.0-update', icon: 'lucide:circle-alert', isContentType: true, order: 6 },
];

export const CONTENT_TYPES: string[] = ['guides'];
export const NAV_BY_KEY: Record<string, NavigationItem> = Object.fromEntries(
  NAVIGATION_CONFIG.map((item) => [item.key, item]),
);
