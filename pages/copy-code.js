(() => {
    function iconMarkup() {
        return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true" class="h-4 w-4"><rect x="9" y="9" width="13" height="13" rx="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>';
    }

    async function copyText(text) {
        if (navigator.clipboard && window.isSecureContext) {
            await navigator.clipboard.writeText(text);
            return;
        }

        const area = document.createElement("textarea");
        area.value = text;
        area.style.position = "fixed";
        area.style.left = "-9999px";
        document.body.appendChild(area);
        area.focus();
        area.select();
        document.execCommand("copy");
        document.body.removeChild(area);
    }

    function wireCopyButtons() {
        const buttons = Array.from(document.querySelectorAll("[data-copy-target]"));
        buttons.forEach((button) => {
            if (!button.dataset.ready) {
                button.dataset.ready = "true";
                button.innerHTML = iconMarkup() + '<span class="text-xs font-semibold">Copy</span>';
            }

            button.addEventListener("click", async () => {
                const targetId = button.getAttribute("data-copy-target");
                const target = document.getElementById(targetId);
                if (!target) {
                    return;
                }

                const original = button.innerHTML;
                try {
                    await copyText(target.textContent || "");
                    button.innerHTML = '<span class="text-xs font-semibold">Copied</span>';
                    setTimeout(() => {
                        button.innerHTML = original;
                    }, 1200);
                } catch (error) {
                    button.innerHTML = '<span class="text-xs font-semibold">Failed</span>';
                    setTimeout(() => {
                        button.innerHTML = original;
                    }, 1200);
                }
            });
        });
    }

    document.addEventListener("DOMContentLoaded", wireCopyButtons);
})();
