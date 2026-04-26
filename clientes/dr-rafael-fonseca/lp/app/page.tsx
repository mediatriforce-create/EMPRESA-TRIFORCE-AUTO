import Image from "next/image";

const WA_LINK = "https://wa.me/5521966832487";

function WhatsAppIcon() {
  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 24 24"
      fill="currentColor"
      className="w-6 h-6"
    >
      <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z" />
    </svg>
  );
}

function CheckIcon() {
  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 20 20"
      fill="currentColor"
      className="w-5 h-5 text-accent flex-shrink-0 mt-0.5"
    >
      <path
        fillRule="evenodd"
        d="M16.704 4.153a.75.75 0 01.143 1.052l-8 10.5a.75.75 0 01-1.127.075l-4.5-4.5a.75.75 0 011.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 011.05-.143z"
        clipRule="evenodd"
      />
    </svg>
  );
}

function CTAButton({
  href,
  children,
  className = "",
  dark = false,
}: {
  href: string;
  children: React.ReactNode;
  className?: string;
  dark?: boolean;
}) {
  return (
    <a
      href={href}
      target="_blank"
      rel="noopener noreferrer"
      className={`inline-flex items-center gap-3 px-8 py-4 rounded-sm font-inter font-700 text-base transition-all duration-200 hover:opacity-90 active:scale-[0.98] ${
        dark
          ? "bg-primary text-soft"
          : "bg-accent text-white"
      } ${className}`}
    >
      <WhatsAppIcon />
      {children}
    </a>
  );
}

/* ─── BLOCO 1: HERO ─── */
function HeroSection() {
  return (
    <section className="relative min-h-screen flex items-center bg-primary overflow-hidden">
      {/* Desktop: split layout */}
      <div className="absolute inset-0 flex">
        {/* Left side gradient */}
        <div className="w-full lg:w-1/2 bg-primary z-10" />
        {/* Right side photo */}
        <div className="hidden lg:block lg:w-1/2 relative">
          <Image
            src="/images/post_06.jpg"
            alt="Dr. Rafael Fonseca - Especialista em Harmonizacao Facial"
            fill
            className="object-cover object-center"
            priority
            sizes="50vw"
          />
          {/* Gradient overlay transitioning left */}
          <div className="absolute inset-0 bg-gradient-to-r from-primary via-primary/60 to-transparent" />
        </div>
      </div>

      {/* Mobile background photo */}
      <div className="absolute inset-0 lg:hidden">
        <Image
          src="/images/post_06.jpg"
          alt="Dr. Rafael Fonseca"
          fill
          className="object-cover object-top"
          priority
          sizes="100vw"
        />
        <div className="absolute inset-0 bg-primary/85" />
      </div>

      {/* Content */}
      <div className="relative z-20 w-full max-w-7xl mx-auto px-6 lg:px-16 py-24 lg:py-32">
        <div className="max-w-xl">
          <p className="font-inter text-accent text-sm font-500 tracking-widest uppercase mb-6">
            Harmonizacao Facial, Corporal e Intima Masculina
          </p>
          <h1 className="font-playfair text-4xl lg:text-6xl text-soft leading-tight mb-6 text-balance">
            Resultado natural. Sem exagero. Sem sair de Marica.
          </h1>
          <p className="font-inter text-mid text-lg leading-relaxed mb-4">
            Dr. Rafael Fonseca e especialista em harmonizacao facial, corporal e
            intima masculina. Atende em Marica e Niteroi. Avaliacao gratuita.
          </p>
          <p className="font-inter text-muted text-base leading-relaxed mb-10">
            Voce merece se sentir bem. Sem parecer que &quot;fez alguma
            coisa&quot;. A estetica que o Dr. Rafael pratica respeita a sua
            face, o seu corpo e a sua historia.
          </p>
          <CTAButton href={WA_LINK}>Agendar avaliacao gratuita no WhatsApp</CTAButton>
        </div>
      </div>
    </section>
  );
}

/* ─── BLOCO 2: PROBLEMA / DOR ─── */
function ProblemSection() {
  return (
    <section className="bg-soft py-20 lg:py-28">
      <div className="max-w-3xl mx-auto px-6 lg:px-8 text-center">
        <h2 className="font-playfair text-3xl lg:text-4xl text-primary mb-8 text-balance">
          Voce quer mudar algo, mas tem medo de exagerar
        </h2>
        <div className="space-y-5 text-body text-lg leading-relaxed font-inter">
          <p>
            Talvez voce olhe no espelho e sinta que algo esta fora do lugar. Nao
            e vaidade. E incomodo real. Mas ai vem o medo: e se ficar
            artificial? E se o medico nao for de confianca?
          </p>
          <p>
            Ou entao voce pensa que estetica boa so existe no Rio ou em
            Niteroi. Que em Marica nao tem profissional de verdade para isso.
          </p>
          <p className="text-primary font-500">
            Esses medos sao comuns. E tem resposta.
          </p>
        </div>
      </div>
    </section>
  );
}

/* ─── BLOCO 3: QUEM E O DR. RAFAEL ─── */
function AboutSection() {
  const bullets = [
    "Especialista em harmonizacao facial e corporal",
    "Unico especialista em harmonizacao intima masculina em Marica",
    "3 anos de consultorio ativo",
    "Atendimento em Marica e Niteroi (Icarai)",
    "Avaliacao gratuita antes de qualquer procedimento",
  ];

  return (
    <section className="bg-mid py-20 lg:py-28">
      <div className="max-w-7xl mx-auto px-6 lg:px-16">
        <div className="grid lg:grid-cols-2 gap-12 lg:gap-20 items-center">
          {/* Text */}
          <div>
            <p className="font-inter text-accent text-sm font-500 tracking-widest uppercase mb-4">
              Quem e o Dr. Rafael
            </p>
            <h2 className="font-playfair text-3xl lg:text-4xl text-primary mb-6 text-balance">
              3 anos formando pacientes satisfeitos em Marica e Niteroi
            </h2>
            <p className="font-inter text-body text-base leading-relaxed mb-6">
              O Dr. Rafael Fonseca e medico especializado em harmonizacao
              facial, corporal e intima masculina. Ele atende em dois
              consultorios: Marica e Icarai, Niteroi.
            </p>
            <p className="font-inter text-body text-base leading-relaxed mb-8">
              Nos ultimos 3 anos, construiu uma pratica baseada em uma ideia
              simples: resultado bonito e resultado que nao grita. Voce sai mais
              confiante. Nao irreconhecivel. Esse e o padrao de trabalho que ele
              chama de{" "}
              <em className="text-primary font-500">
                &quot;estetica com naturalidade&quot;
              </em>
              .
            </p>
            <ul className="space-y-3">
              {bullets.map((item, i) => (
                <li key={i} className="flex items-start gap-3 font-inter text-body text-sm">
                  <CheckIcon />
                  <span>{item}</span>
                </li>
              ))}
            </ul>
          </div>

          {/* Photo */}
          <div className="relative">
            <div className="relative h-[500px] lg:h-[600px] rounded-xl overflow-hidden shadow-2xl">
              <Image
                src="/images/post_07.jpg"
                alt="Dr. Rafael Fonseca em consultorio"
                fill
                className="object-cover object-center"
                sizes="(max-width: 1024px) 100vw, 50vw"
              />
            </div>
            {/* Decorative element */}
            <div className="absolute -bottom-4 -left-4 w-32 h-32 bg-accent/20 rounded-full blur-2xl" />
          </div>
        </div>
      </div>
    </section>
  );
}

/* ─── BLOCO 4: PROCEDIMENTOS ─── */
function ProceduresSection() {
  const procedures = [
    {
      title: "Harmonizacao Facial",
      items: [
        "Botox",
        "Preenchimento labial",
        "Macas do rosto",
        "Contorno queixo e mandibula",
        "Olheiras",
        "Bioestimuladores de colageno",
      ],
    },
    {
      title: "Harmonizacao Corporal",
      items: ["Preenchimento de gluteos", "Bioestimuladores corporais"],
    },
    {
      title: "Harmonizacao Intima Masculina",
      items: [
        "Bioplastia peniana",
        "Preenchimento com acido hialuronico intimo",
      ],
      highlight: true,
    },
  ];

  return (
    <section className="bg-soft py-20 lg:py-28">
      <div className="max-w-7xl mx-auto px-6 lg:px-16">
        <div className="text-center mb-14">
          <p className="font-inter text-accent text-sm font-500 tracking-widest uppercase mb-4">
            Procedimentos
          </p>
          <h2 className="font-playfair text-3xl lg:text-4xl text-primary mb-4 text-balance">
            O que o Dr. Rafael trata
          </h2>
          <p className="font-inter text-muted text-base max-w-xl mx-auto">
            Cada procedimento tem indicacao especifica. Na avaliacao, ele
            explica qual faz sentido para o seu caso.
          </p>
        </div>

        <div className="grid md:grid-cols-3 gap-6 mb-12">
          {procedures.map((proc, i) => (
            <div
              key={i}
              className={`rounded-xl p-8 ${
                proc.highlight
                  ? "bg-primary text-soft border-2 border-accent/40"
                  : "bg-white border border-mid"
              }`}
            >
              <h3
                className={`font-playfair text-xl mb-5 ${
                  proc.highlight ? "text-accent" : "text-primary"
                }`}
              >
                {proc.title}
              </h3>
              <ul className="space-y-2">
                {proc.items.map((item, j) => (
                  <li
                    key={j}
                    className={`flex items-center gap-2 font-inter text-sm ${
                      proc.highlight ? "text-mid" : "text-body"
                    }`}
                  >
                    <span
                      className={`w-1.5 h-1.5 rounded-full flex-shrink-0 ${
                        proc.highlight ? "bg-accent" : "bg-accent/60"
                      }`}
                    />
                    {item}
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>

        {/* Nested CTA */}
        <div className="bg-mid rounded-xl p-8 flex flex-col md:flex-row items-center justify-between gap-6">
          <p className="font-inter text-primary text-base font-500 max-w-lg">
            Nao sabe qual procedimento e para voce? A avaliacao gratuita
            responde isso.
          </p>
          <CTAButton href={WA_LINK} className="whitespace-nowrap">
            Falar com o Dr. Rafael
          </CTAButton>
        </div>
      </div>
    </section>
  );
}

/* ─── BLOCO 5: COMO FUNCIONA ─── */
function HowItWorksSection() {
  const steps = [
    {
      number: "01",
      title: "Avaliacao gratuita",
      body: "Voce entra em contato pelo WhatsApp. O Dr. Rafael agenda uma conversa sem compromisso. Ele entende o que voce quer e explica o que e indicado para o seu caso. Sem pressao. Sem protocolo fixo.",
    },
    {
      number: "02",
      title: "Procedimento com seguranca",
      body: "Tudo feito em consultorio medico. Com materiais certificados e tecnica validada. O Dr. Rafael explica cada etapa antes de comecar.",
    },
    {
      number: "03",
      title: "Resultado que respeita voce",
      body: "O objetivo nao e mudar quem voce e. E eliminar o incomodo que te incomoda. Resultado discreto, natural e duradouro.",
    },
  ];

  return (
    <section className="bg-primary py-20 lg:py-28">
      <div className="max-w-7xl mx-auto px-6 lg:px-16">
        <div className="text-center mb-14">
          <p className="font-inter text-accent text-sm font-500 tracking-widest uppercase mb-4">
            Como funciona
          </p>
          <h2 className="font-playfair text-3xl lg:text-4xl text-soft text-balance">
            Do primeiro contato ao resultado: 3 passos simples
          </h2>
        </div>

        <div className="grid md:grid-cols-3 gap-8 lg:gap-12">
          {steps.map((step, i) => (
            <div key={i} className="flex flex-col items-start">
              {/* Number circle */}
              <div className="w-14 h-14 rounded-full bg-accent flex items-center justify-center mb-6 flex-shrink-0">
                <span className="font-inter font-700 text-white text-lg">
                  {step.number}
                </span>
              </div>
              {/* Connector line desktop */}
              <div className="hidden md:block absolute" />
              <h3 className="font-playfair text-xl text-soft mb-3">
                {step.title}
              </h3>
              <p className="font-inter text-muted text-base leading-relaxed">
                {step.body}
              </p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

/* ─── BLOCO 6: PROVA SOCIAL ─── */
function TestimonialsSection() {
  const testimonials = [
    {
      quote:
        "Eu tinha muito medo de ficar com cara de plastico. O Dr. Rafael me explicou tudo antes, foi fazendo aos poucos, e hoje as pessoas me perguntam se eu estou dormindo bem. Ninguem sabe que fiz nada.",
      info: "Paciente de Marica",
      procedure: "Harmonizacao facial",
    },
    {
      quote:
        "Fui por indicacao e voltei mais duas vezes. Atendimento humano, sem pressa, e resultado que durou muito mais do que eu esperava.",
      info: "Paciente de Icarai",
      procedure: "Bioestimulador de colageno",
    },
    {
      quote:
        "Achei que teria julgamento. Nao teve. O Dr. Rafael tratou como qualquer outro procedimento. Fiquei muito satisfeito com o resultado e com a discricao.",
      info: "Paciente de Marica",
      procedure: "Harmonizacao intima",
    },
  ];

  return (
    <section className="bg-mid py-20 lg:py-28">
      <div className="max-w-7xl mx-auto px-6 lg:px-16">
        <div className="text-center mb-14">
          <p className="font-inter text-accent text-sm font-500 tracking-widest uppercase mb-4">
            Depoimentos
          </p>
          <h2 className="font-playfair text-3xl lg:text-4xl text-primary mb-3 text-balance">
            O que os pacientes dizem depois de 3 anos de consultorio
          </h2>
          <p className="font-inter text-muted text-sm">
            Cada depoimento e de um paciente real de Marica ou Niteroi.
          </p>
        </div>

        <div className="grid md:grid-cols-3 gap-6">
          {testimonials.map((t, i) => (
            <div
              key={i}
              className="bg-soft rounded-xl p-8 flex flex-col justify-between"
            >
              {/* Quote mark */}
              <div>
                <div className="text-accent text-5xl font-playfair leading-none mb-4">
                  &ldquo;
                </div>
                <p className="font-inter text-body text-base leading-relaxed italic mb-6">
                  {t.quote}
                </p>
              </div>
              <div className="flex items-center gap-4 border-t border-mid pt-4">
                {/* Avatar placeholder */}
                <div className="w-10 h-10 rounded-full bg-primary/10 flex items-center justify-center flex-shrink-0">
                  <span className="text-primary font-playfair font-700 text-sm">
                    {t.info.charAt(t.info.lastIndexOf(" ") + 1)}
                  </span>
                </div>
                <div>
                  <p className="font-inter text-primary text-sm font-500">
                    {t.info}
                  </p>
                  <p className="font-inter text-muted text-xs">{t.procedure}</p>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

/* ─── BLOCO 7: HARMONIZACAO INTIMA MASCULINA ─── */
function IntimateSection() {
  return (
    <section className="bg-dark py-20 lg:py-28 overflow-hidden">
      <div className="max-w-7xl mx-auto px-6 lg:px-16">
        <div className="grid lg:grid-cols-2 gap-12 lg:gap-20 items-center">
          {/* Text */}
          <div className="order-2 lg:order-1">
            <p className="font-inter text-accent text-sm font-500 tracking-widest uppercase mb-4">
              Harmonizacao Intima Masculina
            </p>
            <h2 className="font-playfair text-3xl lg:text-4xl text-soft mb-4 text-balance">
              Voce nao e o unico homem que pensa nisso
            </h2>
            <p className="font-inter text-muted text-base mb-8 italic">
              E provavelmente nunca falou com ninguem sobre isso.
            </p>

            <div className="space-y-4 font-inter text-mid text-base leading-relaxed mb-8">
              <p>
                Existe uma parte do corpo que muitos homens gostariam de mudar.
                Mas o assunto parece proibido. Nao tem onde perguntar sem
                constrangimento. Nao sabe se existe tratamento seguro. Nao sabe
                se existe especialista perto de voce.
              </p>
              <p>
                Em Marica, o Dr. Rafael Fonseca e o unico medico que realiza
                harmonizacao intima masculina. O procedimento existe, e seguro,
                e e feito em consultorio medico.{" "}
                <span className="text-soft font-500">
                  Com tecnica, etica e total discricao.
                </span>
              </p>
            </div>

            {/* Procedures */}
            <div className="flex gap-3 mb-8 flex-wrap">
              {["Bioplastia peniana", "Preenchimento com acido hialuronico"].map(
                (p) => (
                  <span
                    key={p}
                    className="bg-primary/60 border border-accent/30 text-mid text-xs font-inter px-4 py-2 rounded-full"
                  >
                    {p}
                  </span>
                )
              )}
            </div>

            {/* Process */}
            <div className="bg-primary/40 border border-accent/20 rounded-xl p-6 mb-8">
              <p className="font-inter text-mid text-sm leading-relaxed mb-3">
                Voce entra em contato pelo WhatsApp. A conversa e privada, so
                entre voce e o consultorio. Na avaliacao, o Dr. Rafael explica
                o procedimento sem julgamento e sem pressa. Voce decide depois,
                sem pressao.
              </p>
            </div>

            {/* Anchor phrase */}
            <p className="font-playfair text-accent text-xl italic mb-8">
              &quot;A maior barreira nao e o procedimento. E a primeira
              mensagem.&quot;
            </p>

            <CTAButton href={WA_LINK}>
              Falar com o Dr. Rafael com discricao
            </CTAButton>
          </div>

          {/* Photo */}
          <div className="order-1 lg:order-2 relative">
            <div className="relative h-[450px] lg:h-[600px] rounded-xl overflow-hidden">
              <Image
                src="/images/post_09.jpg"
                alt="Dr. Rafael Fonseca - Atendimento com discrição e ética"
                fill
                className="object-cover object-center"
                sizes="(max-width: 1024px) 100vw, 50vw"
              />
              <div className="absolute inset-0 bg-gradient-to-t from-dark/60 to-transparent" />
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

/* ─── BLOCO 8: CTA FINAL ─── */
function FinalCTASection() {
  return (
    <section className="bg-accent py-20 lg:py-28">
      <div className="max-w-3xl mx-auto px-6 lg:px-8 text-center">
        <h2 className="font-playfair text-3xl lg:text-5xl text-white mb-6 text-balance">
          Avaliacao gratuita com o Dr. Rafael
        </h2>
        <p className="font-inter text-white/90 text-lg leading-relaxed mb-10">
          Voce nao precisa decidir nada agora. Na avaliacao, ele entende o que
          voce quer e explica o que faz sentido para o seu caso. Sem
          compromisso. Sem protocolo fixo.
        </p>

        {/* Addresses */}
        <div className="flex flex-col sm:flex-row gap-4 justify-center mb-10">
          <div className="bg-white/20 rounded-lg px-6 py-3 font-inter text-white text-sm">
            <span className="block font-500">Marica / RJ</span>
          </div>
          <div className="bg-white/20 rounded-lg px-6 py-3 font-inter text-white text-sm">
            <span className="block font-500">Niteroi (Icarai)</span>
          </div>
          <div className="bg-white/20 rounded-lg px-6 py-3 font-inter text-white text-sm">
            <span className="block font-500">(21) 96683-2487</span>
          </div>
        </div>

        <div className="flex justify-center mb-6">
          <CTAButton href={WA_LINK} dark>
            Agendar avaliacao gratuita no WhatsApp
          </CTAButton>
        </div>

        <p className="font-inter text-white/70 text-sm">
          Atendimento de segunda a sabado. Resposta rapida pelo WhatsApp.
        </p>
      </div>
    </section>
  );
}

/* ─── FOOTER ─── */
function Footer() {
  return (
    <footer className="bg-primary py-8">
      <div className="max-w-7xl mx-auto px-6 lg:px-16">
        <div className="flex flex-col md:flex-row items-center justify-between gap-4">
          <p className="font-inter text-muted text-sm">
            Dr. Rafael Fonseca | CRM-RJ
          </p>
          <p className="font-inter text-muted text-xs text-center">
            Procedimentos esteticos realizados por medico habilitado.
            Resultados podem variar individualmente.
          </p>
          <p className="font-inter text-muted text-sm">
            Marica e Niteroi, RJ
          </p>
        </div>
      </div>
    </footer>
  );
}

/* ─── WHATSAPP FLOATING BUTTON (MOBILE) ─── */
function WhatsAppFloat() {
  return (
    <a
      href={WA_LINK}
      target="_blank"
      rel="noopener noreferrer"
      className="fixed bottom-6 right-6 z-50 lg:hidden bg-[#25D366] text-white w-16 h-16 rounded-full flex items-center justify-center shadow-2xl hover:bg-[#20BA5A] transition-colors active:scale-95"
      aria-label="Falar pelo WhatsApp"
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 24 24"
        fill="currentColor"
        className="w-8 h-8"
      >
        <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z" />
      </svg>
    </a>
  );
}

/* ─── PAGE ─── */
export default function Home() {
  return (
    <main>
      <HeroSection />
      <ProblemSection />
      <AboutSection />
      <ProceduresSection />
      <HowItWorksSection />
      <TestimonialsSection />
      <IntimateSection />
      <FinalCTASection />
      <Footer />
      <WhatsAppFloat />
    </main>
  );
}
