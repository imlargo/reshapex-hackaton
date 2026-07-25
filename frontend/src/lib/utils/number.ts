export function formatCurrency(amount: number, currency = 'USD', locale = 'es'): string {
	return new Intl.NumberFormat(locale, { style: 'currency', currency }).format(amount);
}

export function formatPercent(value: number, locale = 'es'): string {
	return new Intl.NumberFormat(locale, { style: 'percent', maximumFractionDigits: 1 }).format(
		value
	);
}

export function formatNumber(value: number, locale = 'es'): string {
	return new Intl.NumberFormat(locale).format(value);
}

export function formatFileSize(bytes: number): string {
	if (bytes === 0) return '0 B';
	const units = ['B', 'KB', 'MB', 'GB'];
	const exponent = Math.floor(Math.log(bytes) / Math.log(1024));
	return `${(bytes / 1024 ** exponent).toFixed(1)} ${units[exponent]}`;
}
